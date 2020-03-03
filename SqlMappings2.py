import pyparsing

from pyparsing import *

class QuotedParameter(object):
    def __init__(self, result):
        self.value = result[0]

    def value(self):
        self.value

    def __str__(self):
        return "Quoted Parameter: " + self.value

    def __repr__(self):
        return "QuotedParameter('" + self.value + "')"

    def generate(self):
        return self.value

class Parameter(object):
    def __init__(self, result):
        self.value = result[0]

    def value(self):
        self.value

    def __str__(self):
        return "Parameter: " + self.value

    def __repr__(self):
        return "Parameter(" + self.value + ")"

    def generate(self):
        return self.value


# Source and Target
COLUMN_NAME_ID = "column_name"
TABLE_NAME_ID = "table_name"
SOURCE_ID = "source"
TARGET_ID = "target"
separator = Suppress("|")
column_name = Word(alphanums + "_").setResultsName(COLUMN_NAME_ID)
table_name = Word(alphanums + "_").setResultsName(TABLE_NAME_ID)
source = Group(separator + table_name + separator + column_name + separator).setResultsName(SOURCE_ID)
target = Group(separator + table_name + separator + column_name + separator).setResultsName(TARGET_ID)


# Direct Mapping
def replace_multiple_spaces(s, loc, toks):
    toks[0] = ' '.join(toks[0].split()).lower()
    return toks


DIRECT_MAPPING_ID = "direct"
direct_mapping = (CaselessKeyword("directmapping") ^ CaselessKeyword("direct_mapping") ^
                  CaselessKeyword("direct-mapping") ^
                  Regex(r"direct\s+mapping", flags=re.IGNORECASE).setParseAction(replace_multiple_spaces) ^
                  CaselessKeyword("direct")).setResultsName(DIRECT_MAPPING_ID)

DO_NOT_MAP_ID = "do_not_map"
do_not_map = ((CaselessKeyword("DoNotMap") ^ CaselessKeyword("Do_Not_Map") ^
                  CaselessKeyword("Do-Not-Map") ^
                  Regex(r"Do\sNot\sMap", flags=re.IGNORECASE).setParseAction(replace_multiple_spaces))).setResultsName(DO_NOT_MAP_ID)

CONCAT_ID = "concat"
concat_keyword = (CaselessKeyword("concat") ^ CaselessKeyword("concatenate")).setResultsName(CONCAT_ID)

TEST_STACK_ID = "test_stack"
test_stack_keyword = (CaselessKeyword("teststack") ^ CaselessKeyword("test_stack") ^
                  CaselessKeyword("test-stack") ^
                  Regex(r"Test\sStack", flags=re.IGNORECASE).setParseAction(replace_multiple_spaces) ^
                  CaselessKeyword("test")).setResultsName(TEST_STACK_ID)
PARAMETERS_ID = "parameters"
INSTRUCTION_ID = "instruction"
FUNCTION_CALL_ID = "function"
SIMPLE_INSTRUCTION_ID = "simple_instruction"
instruction = Forward()
simple_instruction = direct_mapping | do_not_map
function_call = test_stack_keyword | concat_keyword
integer = Word(nums)
arg = Group(instruction) | function_call | integer | (quotedString.setParseAction(QuotedParameter)) | (Word(alphas, alphanums + "_")).setParseAction(Parameter)
lparen, rparen,  = map(Suppress, "()")
instruction <<= Group(simple_instruction(SIMPLE_INSTRUCTION_ID) ^ (function_call(FUNCTION_CALL_ID) + lparen + Group(Optional(delimitedList(arg)))(PARAMETERS_ID) + rparen)).setResultsName(INSTRUCTION_ID)
mappings = ZeroOrMore(Group(source + instruction + target))


def parse_mappings(s):
    parsed_string = mappings.parseString(s)
    return parsed_string
