import connexion
import six

from swagger_server.models.course import Course  # noqa: E501
from swagger_server import util


def add_course(body, semester, courseCode):  # noqa: E501
    """add_course

    Add a new course to a semester (This can only be done by an authorized admin) # noqa: E501

    :param body: Course object that needs to be added to the Semester
    :type body: dict | bytes
    :param semester: Available Semesters (1, 2, 3, 4, 5, 6, 7, 8, general, technical, short-semester)
    :type semester: str
    :param courseCode: Course Code
    :type courseCode: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = Course.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
