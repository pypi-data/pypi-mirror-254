from emoji import emojize
__version__ = "1.2.2"
__description__ = "Quickly Arrange,Quickly Test!"
__image__ = emojize(fr"""{__description__}:rocket::rocket::rocket:version:{__version__}""")

if __name__ == '__main__':
    print(__image__)