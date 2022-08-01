# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.course import Course  # noqa: E501
from swagger_server.models.course_list import CourseList  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_get_course_by_code(self):
        """Test case for get_course_by_code

        
        """
        response = self.client.open(
            '/dhmudalige/courses/1.0.0/{semester}/{courseCode}/'.format(semester='semester_example', courseCode='courseCode_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_course_details_by_semester(self):
        """Test case for get_course_details_by_semester

        
        """
        response = self.client.open(
            '/dhmudalige/courses/1.0.0/{semester}/'.format(semester='semester_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_courses(self):
        """Test case for get_courses

        
        """
        response = self.client.open(
            '/dhmudalige/courses/1.0.0/',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
