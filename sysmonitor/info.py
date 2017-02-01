import platform

def uname():
    """
    Return a named tuple containing platform information

    Type name: uname_result
    File names (with examples):
        system='Linux',
        node='nikola',
        release='4.4.0-47-generic',
        version='#68~14.04.1-Ubuntu SMP Wed Oct 26 19:42:11 UTC 2016',
        machine='x86_64',
        processor='x86_64'

    For more information see: https://docs.python.org/3/library/platform.html#platform.uname
    """
    return platform.uname()

def uname_asdict():
    """Return uname as dictionary"""
    return uname()._asdict()


if __name__=="__main__":
    print("uname:", uname_asdict())

