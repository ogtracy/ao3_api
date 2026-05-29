from AO3 import Work, utils, Session
import AO3


def find_public_works():
    url = "https://archiveofourown.org/works/79206236/chapters/207814801"
    workid = utils.workid_from_url(url)
    print(f"Work ID: {workid}")
    work = Work(workid)
    print(f"Chapters: {work.nchapters}")

    assert workid == 79206236
    assert work.nchapters == 11


def load_locked_work():
    try:
        url = "https://archiveofourown.org/works/14392692/chapters/33236241"
        workid = utils.workid_from_url(url)
        Work(workid)
    except Exception as e:
        assert isinstance(e, AO3.utils.AuthError)
        print("Loading a locked work without logging in raises AuthError")

def load_hidden_work():
    try:
        url = "https://archiveofourown.org/works/52985041/chapters/134037295"
        workid = utils.workid_from_url(url)
        Work(workid)
    except Exception as e:
        assert isinstance(e, AO3.utils.HiddenWorkError)
        print("Loading a locked work without logging in raises HiddenWorkError")

def load_nonexistent_work():
    try:
        url = "https://archiveofourown.org/works/99999999999999999999"
        workid = utils.workid_from_url(url)
        Work(workid)
    except Exception as e:
        assert isinstance(e, AO3.utils.InvalidIdError)
        print("Loading a non-existent work raises InvalidIdError")

def attempt_incorrect_login():
    try:
        Session("username", "password")
    except Exception as e:
        assert isinstance(e, AO3.utils.LoginError)
        print("Logging in with invalid credentials raises LoginError")

def attempt_login():
    session = Session(input("Username? "), input("password? "))
    # print(f"Bookmarks: {session.bookmarks}")
    url = "https://archiveofourown.org/works/14392692/chapters/33236241"
    workid = utils.workid_from_url(url)
    Work(workid, session=session)


# find_public_works()
load_locked_work()
load_nonexistent_work()
load_hidden_work()
attempt_incorrect_login()
# attempt_login()
