from .Styling.Banners import sd
from .Styling.Colors import bc

class ErrorHandler:
    def __init__(self):
        self.DefinedErrors = [
            # Setup Error Tags
            "dependency_install_failed",
			"ui_file_move_failed"

            # Server Error Tags
            "server_connect_failed",
			"server_change_directory_failed",

            # Database Connection Error Tags
			"database_connect_failed",
			"create_table_failed", # CREATE Table Error Tags
			"invalid_build_statement_type", # SQL Builder Error Tags
			"undefined_table_insert", # INSERT Error Tags
			"execute_insert_failed", # INSERT Error Tags
			"undefined_table_select", # SELECT Error Tags
			"execute_select_failed", # SELECT Error Tags

            # Input Error Tags
            "empty_base_url",
            "invalid_base_url_protocol",

            # Request Error Tags
            "link_not_live",
            "no_response",
            "get_webpage_text_failed",

            # Storage Error Tags (Scanner)
            "storage_textfile_invalid_type",
			"storage_database_invalid_type",
        ]
    
    def Throw(self, ErrorTag: str, ErrorData: str or list = None):
        self.ErrorTag: str = ErrorTag.lower()
        self.ErrorData: str or list = ErrorData

        if(self.ErrorTag in self.DefinedErrors):
            if(self.ErrorTag == "dependency_install_failed"):
                return f"{sd.eBan} Failed to install dependencies from {bc.RC}{self.ErrorData}{bc.BC}\n\n{sd.eBan} Setup failed"
            elif(self.ErrorTag == "ui_file_move_failed"):
                return f"{sd.eBan} Failed to move {bc.RC}{self.ErrorData[0]}/{bc.BC} to {bc.RC}{self.ErrorData[1]}{bc.BC}\n\n{sd.eBan} Setup failed"

            # Server Error Messages
            elif(self.ErrorTag == "server_connect_failed"):
                return f"{sd.eBan} Failed to connect to the {bc.RC}{self.ErrorData}{bc.BC} server\n"
            elif(self.ErrorTag == "server_change_directory_failed"):
                return f"\n{sd.eBan} Failed to change directory to {bc.RC}{self.ErrorData}{bc.BC}\n"

            # Database Connection Error Messages
            elif(self.ErrorTag == "database_connect_failed"):
                return f"{sd.eBan} Failed to connect to the Database {bc.RC}{self.ErrorData}{bc.BC}"

            # CREATE Table Error Messages
            elif(self.ErrorTag == "create_table_failed"):
                return f"{sd.eBan} Failed to create Database table {bc.RC}{self.ErrorData}{bc.BC}"

            # SQL Builder Error Messages
            elif(self.ErrorTag == "invalid_build_statement_type"):
                return f"{sd.eBan} Invalid Build SQL Statement Type {bc.RC}{self.ErrorData}{bc.BC}. Allowed Types: select, insert, update, delete"

            # INSERT Error Messages
            elif(self.ErrorTag == "undefined_table_insert"):
                return f"{sd.eBan} Failed to insert data into Database, undefined table name {bc.RC}{self.ErrorData}{bc.BC}"
            elif(self.ErrorTag == "execute_insert_failed"):
                return f"{sd.eBan} Failed to insert data into Database table {bc.RC}{self.ErrorData}{bc.BC}"

            # SELECT Error Messages
            elif(self.ErrorTag == "undefined_table_select"):
                return f"{sd.eBan} Failed to select data from Database, undefined table name {bc.RC}{self.ErrorData}{bc.BC}"
            elif(self.ErrorTag == "execute_select_failed"):
                return f"{sd.eBan} Failed to select data from Database table {bc.RC}{self.ErrorData}{bc.BC}"
            
            # Input Error Messages
            elif(self.ErrorTag == "empty_base_url"):
                return f"{sd.eBan} Base URL value cannot be empty\n"
            elif(self.ErrorTag == "invalid_base_url_protocol"):
                return f"{sd.eBan} Invalid Base URL protocol, must start with {bc.GC}http://{bc.BC} or {bc.GC}https://{bc.BC}\n"

            # Request Error Messages
            elif(self.ErrorTag == "link_not_live"):
                return f"{sd.eBan} URL {bc.RC}{self.ErrorData}{bc.BC} is not live"
            elif(self.ErrorTag == "no_response"):
                return f"{sd.eBan} Got no response from {bc.RC}{self.ErrorData}{bc.BC}"
            elif(self.ErrorTag == "get_webpage_text_failed"):
                return f"{sd.eBan} Failed to get webpage text from {bc.RC}{self.ErrorData}{bc.BC}"

            # Storage Error Messages (Scanner)
            elif(self.ErrorTag == "storage_textfile_invalid_type"):
                return f"{sd.eBan} Textfile Storage Type {bc.RC}{self.ErrorData}{bc.BC} is invalid, it should be {bc.GC}text_file{bc.BC}"
            elif(self.ErrorTag == "storage_database_invalid_type"):
                return f"{sd.eBan} Database Storage Type {bc.RC}{self.ErrorData}{bc.BC} is invalid, it should be {bc.GC}database{bc.BC}"

            else:
                return f"{sd.eBan} Undefined Error Message for Error Tag {bc.RC}{self.ErrorTag}{bc.BC}\n"
        else:
            return f"{sd.eBan} Undefined, Error Tag {bc.RC}{self.ErrorTag}{bc.BC} not found\n"
