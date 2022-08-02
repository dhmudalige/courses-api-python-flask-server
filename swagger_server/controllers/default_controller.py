import connexion
import six

from swagger_server.models.course import Course  # noqa: E501
from swagger_server.models.course_list import CourseList  # noqa: E501
from swagger_server.models.semester import Semester  # noqa: E501
from swagger_server import util


def get_course_by_code(semester, courseCode):  # noqa: E501
    """get_course_by_code

    Returns the details of the specified course # noqa: E501

    :param semester: Available Semesters (1, 2, 3, 4, 5, 6, 7, 8, general, technical, short-semester)
    :type semester: str
    :param courseCode: Course Code
    :type courseCode: str

    :rtype: Course
    """
    return 'do some magic!'


def get_course_details_by_semester(semester):  # noqa: E501
    """get_course_details_by_semester

    Retuns the list of available courses the specified semester # noqa: E501

    :param semester: Available Semesters (1, 2, 3, 4, 5, 6, 7, 8, general, technical, short-semester)
    :type semester: str

    :rtype: CourseList
    """
    return 'do some magic!'


def get_courses():  # noqa: E501
    """get_courses

    Retuns the list of all available courses (Group by semesters) # noqa: E501


    :rtype: Semester
    """
    return 'do some magic!'
