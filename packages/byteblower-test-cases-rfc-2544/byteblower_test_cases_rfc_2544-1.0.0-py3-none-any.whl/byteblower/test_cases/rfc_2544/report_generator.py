from datetime import datetime, timedelta
from os.path import abspath, dirname, join
from typing import Dict, List

import jinja2
import pandas as pd
from byteblower_test_framework import __version__ as framework_version
from byteblowerll.byteblower import ByteBlower
from highcharts_excentis import Highchart

from .definitions import DEFAULT_TRIAL_DURATION, MAX_ITERATIONS

try:
    import simplejson as json
except ImportError:
    import json

_PACKAGE_DIRECTORY = dirname(abspath(__file__))

_QUOTES = [
    (
        "The greatest glory in living lies not in never falling," +
        "<br>but in rising every time we fall.",
        "ByteBlower rises with you, optimizing networks" +
        "<br>to new heights of success.",
    ),
    (
        "In the journey of a thousand miles," +
        "<br>the first step is the most important.",
        "Begin your network optimization journey" +
        " with ByteBlower, your trusted guide.",
    ),
    (
        "Success is not final, failure is not fatal:" +
        "<br>It is the courage to continue that counts.",
        "ByteBlower empowers you to persevere" +
        "<br>in the pursuit of network perfection.",
    ),
    (
        "Believe you can and you're halfway there.",
        "ByteBlower believes in your network's potential," +
        " working tirelessly to ensure it reaches its destination.",
    ),
    (
        "The only limit to our realization of tomorrow" +
        "<br>will be our doubts of today.",
        "With ByteBlower by your side, doubtlessly" +
        "<br>forge ahead to unlock network excellence.",
    ),
    (
        "Embrace the challenges that come your way," +
        "<br>for they are the stepping stones" + "<br>to greatness.",
        "ByteBlower, your faithful companion in the world of testing, is here"
        + "<br>to help you conquer those challenges," +
        " one network improvement at a time",
    ),
]


def timedelta_to_seconds(timedelta: timedelta):
    return timedelta.total_seconds()


def timedelta_to_str(timedelta: timedelta):
    return str(timedelta)[:-4]


def format_datetime_iso(dt: datetime):
    return dt.isoformat()


_JINJA2_ENV = jinja2.Environment(loader=jinja2.FileSystemLoader(
    searchpath=join(_PACKAGE_DIRECTORY, 'templates')))
_JINJA2_ENV.filters['total_seconds'] = timedelta_to_seconds
_JINJA2_ENV.filters['iso_format'] = format_datetime_iso
_JINJA2_ENV.filters['str'] = timedelta_to_str
_TEMPLATE = _JINJA2_ENV.get_template("report.html")


def _chart_options(x_axis: Dict, title: str, y_axis: List[Dict]) -> Dict:
    if not isinstance(title, str):
        raise TypeError()
    options = {
        "chart": {
            "zoomType": "xy"
        },
        "title": {
            "text": title,
            "align": "center"
        },
        "xAxis": [{
            "title": {
                "text": x_axis['text'],
                "style": {
                    "color": "black"
                }
            },
            "categories": x_axis['values'],
        }],
        "yAxis": [{
            "labels": {
                "format": "{value}" + y_axis[0].get("value", "Mb/s"),
                "style": {
                    "color": "Highcharts.getOptions().colors[0]"
                }
            },
            "title": {
                "text": y_axis[0].get("text", "Bitrate"),
                "style": {
                    "color": "Highcharts.getOptions().colors[0]"
                }
            },
            "min": y_axis[0].get("min", 0),
        }]
    }
    if len(y_axis) > 1:
        options["yAxis"].append({
            "title": {
                "text": y_axis[1].get("text", "Frame loss"),
                "style": {
                    "color": "Highcharts.getOptions().colors[1]"
                }
            },
            "labels": {
                "format": "{value}" + y_axis[1].get("value", "%"),
                "style": {
                    "color": "Highcharts.getOptions().colors[1]"
                }
            },
            "min": y_axis[1].get("min", 0),
            "opposite": "true"
        })
    options['legend'] = {'align': 'center', 'verticalAlign': 'bottom'}
    return options


def _summary_plot_generator(
    result_dict: List[Dict],
    plot_name: str,
    title: str,
    yaxis: List[Dict],
    series=List[Dict],
):
    # data preparation
    x_axis = {"values": [x['size'] for x in result_dict], 'text': 'Frame size'}
    chart = Highchart(renderTo=plot_name)
    chart.set_dict_options(_chart_options(x_axis, title, yaxis))
    for serie in series:
        if serie['data'] == 'trials':
            data = [len(x[serie['data']]) for x in result_dict]
        elif serie['data'] == 'test_duration':
            data = [
                round(pd.Timedelta(x[serie['data']]).total_seconds())
                for x in result_dict
            ]
        else:
            data = [round(x[serie['data']] / 1e6, 2) for x in result_dict]
        chart.add_data_set(
            data=data,
            series_type=serie.get('series_type', 'column'),
            name=serie['title'],
            yAxis=serie.get('yaxis', 0),
            tooltip={'valueSuffix': serie.get('valueSuffix', '')})
    chart.buildhtml()
    return chart.content


def _final_plots_generator(results: List[Dict]):
    plot1 = [{
        'data': 'real_bitrate',
        'title': 'Tested bitrate',
        'valueSuffix': 'Mb/s'
    }, {
        'data': 'expected_bitrate',
        'title': 'Expected bitrate',
        'valueSuffix': 'Mb/s'
    }]
    plot2 = [{
        'data': 'trials',
        'title': 'Number of Trials',
    }, {
        'data': 'test_duration',
        'title': 'Test duration',
        "type": 'datetime',
        "labels": {
            "formatter":
            """
                    function() {
                        var seconds = this.value % 60 ;
                        var minutes = Math.floor((this.value / 60 ) % 60);
                        var hours = Math.floor(this.value / 3600);
                        return hours + 'h ' + minutes + 'm ' + seconds + 's';
                    }
                    """
        },
        'yaxis': 1,
    }]
    yaxis = [{
        'text': 'Trials',
        'value': ''
    }, {
        'text': 'Duration',
        'value': 's'
    }]

    return [
        _summary_plot_generator(
            result_dict=results,
            plot_name='plot1',
            title='Real vs Expected throughputs',
            yaxis=[{}],
            series=plot1,
        ),
        _summary_plot_generator(
            result_dict=results,
            plot_name='plot2',
            title='Duration & number Trials per frame size',
            yaxis=yaxis,
            series=plot2)
    ]


def _frame_plot_generator(result_dict: Dict, series_type: str = 'spline'):
    # data & config preparation
    frame_loss = [
        round(1 - x['rx_packets'] / x['tx_packets'], 4) * 100
        for x in result_dict['trials']
    ]
    bitrates = [round((x["bitrate"] / 1e6), 4) for x in result_dict['trials']]
    # Values of the x axis
    x_axis = {
        "values": [x + 1 for x in range(len(result_dict['trials']))],
        'text': 'Trials'
    }
    # Other configuration of the y axis
    y_axis = [{'min': 0}, {'min': 0, 'text': 'Frame loss', 'value': '%'}]

    # Generate the charts
    chart = Highchart(renderTo="plot_" + str(result_dict['size']))
    chart.set_dict_options(
        _chart_options(x_axis, "Tested bitrate & Frame loss per iteration",
                       y_axis))
    chart.add_data_set(data=bitrates,
                       series_type=series_type,
                       name='Tested bitrate',
                       tooltip={'valueSuffix': 'Mb/s'})
    chart.add_data_set(data=frame_loss,
                       series_type=series_type,
                       name='Frame loss',
                       yAxis=1,
                       tooltip={'valueSuffix': '%'})
    # Building and returning the js code of the charts
    chart.buildhtml()
    return chart.content


def html_report_generator(
    configuration: Dict,
    results: List[Dict],
    errors: Dict,
    output_file: str,
    status: bool = False,
    max_ieration: int = MAX_ITERATIONS,
    iteration_duration: int = DEFAULT_TRIAL_DURATION,
) -> None:
    """Generate HTML report file based on RFC 2544 throughput test results.

    :param configuration: Setup configuration (ByteBlower server,
       source & destination configurations)
    :type configuration: Dict
    :param results: Set of results of all simulations
    :type results: List[Dict]
    :param errors: Set of errors during all simulations
    :type errors: Dict
    :param output_file: path + prefix of the HTML output file
    :type output_file: str
    :param status: Test status (True if no error occurs), defaults to False
    :type status: bool, optional
    :param max_ieration: Max number of test iteration per frame size,
       defaults to :const:`MAX_ITERATIONS`
    :type max_ieration: int, optional
    :param iteration_duration: duration of one iteration in seconds,
       defaults to :const:`DEFAULT_TRIAL_DURATION`
    :type iteration_duration: int, optional
    """
    #Total duration of the entire test
    total_test_duration = sum([x["test_duration"] for x in results],
                              timedelta())
    # Generate the summary plots
    summary_plots = _final_plots_generator(results)

    # Detailed results + plots for each frame size
    container = [{
        "plot": _frame_plot_generator(frame),
        "frame": frame
    } for frame in results]

    api_version = ByteBlower.InstanceGet().APIVersionGet()
    chart = Highchart(offline=True)
    chart.buildhtmlheader()
    js_resources = chart.htmlheader
    quote_head, quote_tagline = _QUOTES[0]

    jinja_data = {
        "quote_head": quote_head,
        "quote_tagline": quote_tagline,
        "api_version": api_version,
        "framework_version": framework_version,
        "js_resources": js_resources,
        "server": configuration["server"],
        "results": container,
        "source": configuration["source"],
        "destination": configuration["destination"],
        "test_duration": total_test_duration,
        "max_ieration": max_ieration,
        "iteration_duration": iteration_duration,
        "summary_plots": summary_plots,
        "errors": errors,
        "status": status
    }
    # input(f"HTML results status is {status}")
    # generate and save the HTML report file
    with open(output_file, "w") as f:
        f.write(_TEMPLATE.render(jinja_data))


def json_report_generator(results: Dict, output_file: str) -> None:
    """Generate a JSON report file based on RFC 2544 throughput test results.

    :param results: Set of: Used test configuration, results of
       all simulations, test status, and error logs
    :type results: Dict
    :param output_file: path + prefix of the JSON output file
    :type output_file: str
    """
    # input(f"JSON results status is {results['status']}")
    pd_series = pd.Series(results)
    pd_series.to_json(output_file, indent=4, date_format='iso')
