import connexion
import six

from swagger_server import util


def update_course(semester, courseCode):  # noqa: E501
    """update_course

    Update course details (This can only be done by an authorized admin) # noqa: E501

    :param semester: Available Semesters (1, 2, 3, 4, 5, 6, 7, 8, general, technical, short-semester)
    :type semester: str
    :param courseCode: Course Code
    :type courseCode: str

    :rtype: None
    """
    return 'do some magic!'
