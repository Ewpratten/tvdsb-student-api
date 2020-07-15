import requests
import re
from ..auth import Student, LoginCreds, getStudent
from typing import List

def getPaymentInfo(creds: LoginCreds) -> dict:

    # Make auth to get student info
    student: Student = getStudent(creds)

    # Make payment request
    data = student._session.get("https://schoolapps2.tvdsb.ca/students/portal_secondary/student_Info/school_cash_info.asp")

    # Parse payment info
    payment = re.findall(r"<td>([0-9]{10})", data.text, re.M)

    return {
        "pin": payment[0]
    }