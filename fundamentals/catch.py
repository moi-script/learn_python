
# try  -> block the code for error
# except -> handle the error
# else -> execute code when no error
# finally -> execute code regardless of result
import logging

logging.basicConfig(level=logging.ERROR)


def testTry () :
    try :
        x = 10
        print(x)
    except :
        print("An error occured")
    else :
        print("hello")
    finally :
        print("FInals")       
    
testTry()




# best cases -> opening or running a short memory that needs to closed 



def openFile(fileName) :
    try :
        o = open(fileName, 'a')
        try :
            o.write("\nHello world")
        except Exception as e : 
            logging.error(f"Unable to write in the file {e}")
        finally : 
            o.close()
    except Exception as e : 
        print("Unable to open file")
        logging.error(f"Unable to write in the file {e}")
  
openFile("test.txt")    
    