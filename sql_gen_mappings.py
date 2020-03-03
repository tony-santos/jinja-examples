class DirectMap():
    def __init__(self, source_table, source_variable, target_table, target_variable):
        self.source_table = source_table
        self.source_variable = source_variable
        self.target_table = target_table
        self.target_variable = target_variable

    def generate_select_code(self):
        pass

    def generate_join_code(self):
        pass

    def generate_where_code(self):
        pass


class Concat():
    def __init__(self, source_table, source_variable, target_table, target_variable):
        self.source_table = source_table
        self.source_variable = source_variable
        self.target_table = target_table
        self.target_variable = target_variable

    def generate_select_code(self):
        pass

    def generate_join_code(self):
        pass

    def generate_where_code(self):
        pass


class TestStack():
    def __init__(self, source_table, source_variable, target_table, target_variable):
        self.source_table = source_table
        self.source_variable = source_variable
        self.target_table = target_table
        self.target_variable = target_variable

    def generate_select_code(self):
        pass

    def generate_join_code(self):
        pass

    def generate_where_code(self):
        pass
