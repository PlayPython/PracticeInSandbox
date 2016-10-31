import jsonpickle
import json

class JsonFormatter(object):
    def __init__(self, file_name, indentation):
        self.file_name = file_name
        # Generally, indentation is 4, or 2
        self.indentation = indentation

    def format_json(self):
        with open(self.file_name, encoding="utf-8", mode='r') as f:
            content = f.read()
            json.dump(content, 's.json')
            # json_content = jsonpickle.encode(content)
            # f.write(json_content)



        # # To see if begins wrongly or ends wrongly
        # if content[0] != '{' or content[len(content) - 1] != '}':
        #     raise "The content has wrong start or end."
        # # Get inside content with removing '{' and '}'
        # content_inside = content[1:len(content) - 1]
        # if len(content_inside) == 0:
        #     return content
        # new_string = '{' + '\n' + ' ' * self.indentation
        # left_string = content_inside
        # while left_string != '':
        #     index = content_inside.find(':')
        #     new_string += content_inside[:index + 1]
        #     left_string = content_inside[index + 1:]
        #     if left_string.strip().find('null,') == 0:
        #         new_string += 'null,' + '\n' + ' ' * self.indentation
        #         left_string = left_string[5:]
        #     if left_string.strip().find('\"') == 0:
        #         end_index = left_string.find('\",')
        #         new_string += left_string[:end_index + 2] + '\n' + ' ' * self.indentation
        #         left_string = left_string[end_index + 2:]
        #     if left_string.strip().find('[{') == 0:








if __name__ == '__main__':
    o = JsonFormatter("s.txt", 4)
    o.format_json()
