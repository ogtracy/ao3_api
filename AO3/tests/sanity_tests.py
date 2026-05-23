from AO3 import Work, utils, Session
import AO3
from AO3.utils import LoginError


def find_public_works():
    url = "https://archiveofourown.org/works/79206236/chapters/207814801"
    workid = utils.workid_from_url(url)
    print(f"Work ID: {workid}")
    work = Work(workid)
    print(f"Chapters: {work.nchapters}")

    assert workid == 79206236
    assert work.nchapters == 11


def load_logged_in_work():
    try:
        url = "https://archiveofourown.org/works/14392692/chapters/33236241"
        workid = utils.workid_from_url(url)
        work = Work(workid)
    except Exception as e:
        assert e is utils.AuthError

def attempt_login():
    session = Session(input("Username? "), input("password? "))
    print(f"Bookmarks: {session.bookmarks}")
    url = "https://archiveofourown.org/works/14392692/chapters/33236241"
    workid = utils.workid_from_url(url)
    work = Work(workid, session=session)

def attempt_incorrect_login():
    try:
        session = Session("username", "password")
        print(f"Bookmarks: {session.bookmarks}")
        url = "https://archiveofourown.org/works/14392692/chapters/33236241"
        workid = utils.workid_from_url(url)
        work = Work(workid, session=session)
    except Exception as e:
        assert isinstance(e, AO3.utils.LoginError)


#find_public_works()
#load_logged_in_work()
attempt_login()
# attempt_incorrect_login()