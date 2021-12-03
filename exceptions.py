import logging
logger = logging.getLogger(__name__)

# def subTask():
#     try:
#         raise ValueError
#     except Exception as e:
#         print('exception raised sub task')
#         # logger.exception(e)
#         raise 

# def main():
#     try:
#         # raise ValueError
#         subTask()
#     except Exception as e:
#         print('exception raised main')
#         # logger.exception(e)
#         # raise
#     print("main returned")

def main():
    try:
        print('before raise')
        raise ValueError
    except Exception as e:
        raise
        print('after raise in exception')


main()