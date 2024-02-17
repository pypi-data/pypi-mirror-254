# Just an example and basic test tool for the 'example.py' module that will test each api endpoint individually by command.

import cmd
import os
import example as test

file_paths = "file_paths.yaml"
   

class TestCmdInterface(cmd.Cmd):
    """command interface"""

    prompt = "PolygonTestCMD$"

    def do_help(self, arg):
        keywords =  ["rsi - relative strength index",
                     "sma - simple moving average",
                     "ema - exponential moving average",
                     "tickerv3 - view detailed information for one select ticker"
                     "tickers - view tickers (defaults to all)",
                     "contracts - display options contracts (defaults to all)",
                     "contract - display one select options contract",
                     "macd - moving average convergence/divergence"
                     "cwd - get the program's current working directory",
                    ]
        print("\nType keyword > Enter to test api endpoint. Customize request parameters in request_parameters.yaml!")
        print("     To paginate over the desired endpoint's data, type the command - '[keyword] -p'")
        print("\n" + "KEYWORDS: " + "\n")
        for keyword in keywords:
            print(keyword)


    def do_rsi(self, arg):
        if arg == "-p":
            test.test_pagination("relative_strength_index")
        elif arg == "":
            test.test("relative_strength_index")
        else:
            print("Invalid argument!")
        return
    
    def do_sma(self, arg):
        if arg == "-p":
            test.test_pagination("simple_moving_average")
        elif arg == "":
            test.test("simple_moving_average")
        else:
            print("Invalid argument!")
        return
    
    def do_ema(self, arg):
        if arg == "-p":
            test.test_pagination("exponential_moving_average")
        elif arg == "":
            test.test("exponential_moving_average")
        else:
            print("Invalid argument!")
        return

    def do_macd(self, arg):
        if arg == "-p":
            test.test_pagination("macd")
        elif arg == "":
            test.test("macd")
        else:
            print("Invalid argument")
        return
    
    def do_contracts(self, arg):
        if arg =="-p":
            test.test_pagination("options_contracts")
        elif arg == "":
            test.test("options_contracts")
        else:
            print("Invalid argument!")
        return
    
    def do_contract(self, arg):
        test.test("options_contract")
        return

    def do_tickers(self, arg):
        if arg == "-p":
            test.test_pagination("view_tickers")
        elif arg == "":
            test.test("view_tickers")
        else:
            print("Invalid argument!")
        return
    
    def do_tickerv3(self, arg):
        test.test("ticker_v3")
        return

    def do_cwd(self, arg):
        print(os.getcwd())

    
cli = TestCmdInterface()
cli.cmdloop()

