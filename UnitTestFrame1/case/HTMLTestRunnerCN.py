# coding=utf-8
"""
HTMLTestRunnerCN 中文版
基于 Wai Yip Tung 原作修改
版本: 1.3.2.CN
"""

import sys
import io
import time
import unittest
from xml.sax import saxutils
import datetime

class OutputRedirector(object):
    """ 输出重定向器 """
    def __init__(self, fp):
        self.fp = fp

    def write(self, s):
        self.fp.write(s)

    def writelines(self, lines):
        self.fp.writelines(lines)

    def flush(self):
        self.fp.flush()

stdout_redirector = OutputRedirector(sys.stdout)
stderr_redirector = OutputRedirector(sys.stderr)

class Template_mixin(object):
    """ 模板混入类 """
    STATUS = {
        0: '通过',
        1: '失败',
        2: '错误',
    }

    DEFAULT_TITLE = '自动化测试报告'
    DEFAULT_DESCRIPTION = '用例执行详情'
    DEFAULT_TESTER = '测试团队'

    HTML_TMPL = r"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html>
<head>
    <title>%(title)s</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://cdn.bootcdn.net/ajax/libs/twitter-bootstrap/4.5.3/css/bootstrap.min.css" rel="stylesheet">
    <style>
    body { font-family: Microsoft YaHei, SimSun, sans-serif; padding: 20px; }
    .heading { margin-bottom: 20px; }
    #result_table { margin-top: 20px; }
    .testcase { margin-left: 1em; }
    .progress { height: 25px; margin: 20px 0; }
    </style>
</head>
<body>
    <div class="container">
        %(heading)s
        %(report)s
        %(ending)s
    </div>
    <script src="https://cdn.bootcdn.net/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script src="https://cdn.bootcdn.net/ajax/libs/twitter-bootstrap/4.5.3/js/bootstrap.min.js"></script>
    <script>
    function showCase(type) {
        $('tr').each(function(){
            $(this).toggle(
                type === 'all' || 
                (type === 'pass' && $(this).hasClass('table-success')) ||
                (type === 'fail' && $(this).hasClass('table-danger')) ||
                (type === 'error' && $(this).hasClass('table-warning'))
            );
        });
    }
    </script>
</body>
</html>
"""

    HEADING_TMPL = """
    <div class="heading">
        <h2 class="text-center">%(title)s</h2>
        <div class="alert alert-info">
            %(parameters)s
            <p class="description">%(description)s</p>
        </div>
        <div class="progress">
            <div class="progress-bar bg-success" style="width: %(pass_rate)s%%">%(Pass)s</div>
            <div class="progress-bar bg-danger" style="width: %(fail_rate)s%%">%(fail)s</div>
            <div class="progress-bar bg-warning" style="width: %(error_rate)s%%">%(error)s</div>
        </div>
    </div>
    """

    HEADING_ATTRIBUTE_TMPL = """
    <p class="attribute"><strong>%(name)s：</strong> %(value)s</p>
    """

    REPORT_TMPL = """
    <table id="result_table" class="table table-bordered table-hover">
        <thead class="thead-dark">
            <tr>
                <th>用例模块</th>
                <th>用例总数</th>
                <th>通过</th>
                <th>失败</th>
                <th>错误</th>
                <th>详细</th>
            </tr>
        </thead>
        <tbody>
            %(test_list)s
        </tbody>
    </table>
    """

    REPORT_CLASS_TMPL = """
    <tr class="%(tr_class)s">
        <td>%(desc)s</td>
        <td>%(count)s</td>
        <td>%(Pass)s</td>
        <td>%(fail)s</td>
        <td>%(error)s</td>
        <td><a href="javascript:void(0)" onclick="$(this).next().toggle()">详细</a>
            <div class="testcase" style="display:none">
                %(test_details)s
            </div>
        </td>
    </tr>
    """

    REPORT_TEST_DETAILS_TMPL = """
    <div>%(desc)s: <span class="badge badge-%(cls)s">%(status)s</span></div>
    """

class _TestResult(unittest.TestResult):
    def __init__(self, verbosity=1):
        super().__init__()
        self.success_count = 0
        self.failure_count = 0
        self.error_count = 0
        self.verbosity = verbosity
        self.result = []

    def startTest(self, test):
        super().startTest(test)
        self.outputBuffer = io.StringIO()
        stdout_redirector.fp = self.outputBuffer
        stderr_redirector.fp = self.outputBuffer

    def complete_output(self):
        output = self.outputBuffer.getvalue()
        self.outputBuffer.seek(0)
        self.outputBuffer.truncate()
        return output

    def stopTest(self, test):
        self.complete_output()

    def addSuccess(self, test):
        self.success_count += 1
        super().addSuccess(test)
        self.result.append((0, test, self.complete_output(), ''))

    def addFailure(self, test, err):
        self.failure_count += 1
        super().addFailure(test, err)
        self.result.append((1, test, self.complete_output(), self._exc_info_to_string(err, test)))

    def addError(self, test, err):
        self.error_count += 1
        super().addError(test, err)
        self.result.append((2, test, self.complete_output(), self._exc_info_to_string(err, test)))

class HTMLTestRunnerCN(Template_mixin):
    def __init__(self, stream=sys.stdout, title=None, description=None, tester=None):
        self.stream = stream  # 新增关键代码[1](@ref)
        if title is not None and not isinstance(title, str):
            raise ValueError("title 参数必须是字符串")
        self.title = title or self.DEFAULT_TITLE
        self.description = description or self.DEFAULT_DESCRIPTION
        self.tester = tester or self.DEFAULT_TESTER
        self.startTime = datetime.datetime.now()

    def run(self, test):
        result = _TestResult()
        test(result)
        self.stopTime = datetime.datetime.now()
        self.generateReport(result)
        return result

    def generateReport(self, result):
        report_attrs = self.getReportAttributes(result)
        heading = self._generate_heading(report_attrs)
        report = self._generate_report(result)
        ending = self._generate_ending()
        html = self.HTML_TMPL % dict(
            title=saxutils.escape(self.title),
            heading=heading,
            report=report,
            ending=ending,
        )
        self.stream.write(html.encode('utf8'))

    def getReportAttributes(self, result):
        total = result.success_count + result.failure_count + result.error_count
        pass_rate = result.success_count / total * 100 if total > 0 else 0.0
        fail_rate = result.failure_count / total * 100 if total > 0 else 0.0
        error_rate = result.error_count / total * 100 if total > 0 else 0.0

        return {
            'title': str(self.title),
            'tester': self.tester,
            'start_time': self.startTime.strftime("%Y-%m-%d %H:%M:%S"),
            'duration': str(self.stopTime - self.startTime),
            'pass_rate': "%.2f%%" % pass_rate,
            'fail_rate': "%.2f%%" % fail_rate,
            'error_rate': "%.2f%%" % error_rate,
            'total': total,
            'Pass': result.success_count,
            'fail': result.failure_count,
            'error': result.error_count,
        }

    def _generate_heading(self, attrs):
        return self.HEADING_TMPL % {
            'title': saxutils.escape(attrs['title']),
            'parameters': ''.join(self.HEADING_ATTRIBUTE_TMPL % {
                'name': name,
                'value': saxutils.escape(str(value))
            } for name, value in [
                ('测试人员', attrs['tester']),
                ('开始时间', attrs['start_time']),
                ('运行时长', attrs['duration']),
                ('用例总数', attrs['total']),
            ]),
            'description': saxutils.escape(self.description),
            'pass_rate': attrs['pass_rate'],
            'fail_rate': attrs['fail_rate'],
            'error_rate': attrs['error_rate'],
            'Pass': attrs['Pass'],
            'fail': attrs['fail'],
            'error': attrs['error'],
        }

    def _generate_report(self, result):
        test_list = []
        sortedResult = self.sortResult(result.result)
        for cid, (cls, cls_results) in enumerate(sortedResult):
            test_details = []
            for tid, (n, t, o, e) in enumerate(cls_results):
                status = self.STATUS[n]
                test_details.append(self.REPORT_TEST_DETAILS_TMPL % {
                    'cls': 'success' if n == 0 else 'danger' if n == 1 else 'warning',
                    'status': status,
                    'desc': t.id().split('.')[-1]
                })

            test_list.append(self.REPORT_CLASS_TMPL % {
                'tr_class': 'table-success' if not any(r[0] > 0 for r in cls_results)
                else 'table-danger' if any(r[0] == 1 for r in cls_results)
                else 'table-warning',
                'desc': cls.__module__ + "." + cls.__name__,
                'count': len(cls_results),
                'Pass': sum(1 for r in cls_results if r[0] == 0),
                'fail': sum(1 for r in cls_results if r[0] == 1),
                'error': sum(1 for r in cls_results if r[0] == 2),
                'test_details': ''.join(test_details)
            })

        return self.REPORT_TMPL % {'test_list': ''.join(test_list)}

    def sortResult(self, result_list):
        rmap = {}
        classes = []
        for n, t, o, e in result_list:
            cls = t.__class__
            if cls not in rmap:
                rmap[cls] = []
                classes.append(cls)
            rmap[cls].append((n, t, o, e))
        return [(cls, rmap[cls]) for cls in classes]

    def _generate_ending(self):
        return "<p class='text-muted text-center'>Generated by HTMLTestRunnerCN</p>"