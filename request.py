import re


def makeLoginAttempt(session, u, p):
    response = session.post(
        "https://campus.ops.org/campus/verify.jsp", data={"username": u, "password": p, "appName": "ops", "url": "nav-wrapper", "lang": "en", "portalLoginPage": "students"})


def getGrades(session):
    return session.get("https://campus.ops.org/campus/resources/portal/grades").json()


def getNotificationNum(session):
    text = session.get("https://campus.ops.org/campus/prism",
                       params={"x": "notifications.NotificationUser-countUnviewed"}).text
    return re.search("(<RecentNotifications.*</RecentNotifications>)", text)
