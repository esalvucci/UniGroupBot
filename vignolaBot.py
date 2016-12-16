import sys
import telepot
from telepot.delegate import per_inline_from_id, create_open, pave_event_space
import random
import vignolaBotToken

foo = ['E\' bugggggia', 'uagliooo!', 'stasera devo programmare...', 'st\'Arduino!', 'Uaglio so arrivat ',
           'eeeeeeeee credo di si...no buggia, \'sto weekend sto con Azzurra',
           'Tonno e cipodda per fa lu soffrittu..capi\'?', 'Non posso venire devo fare la valigia',
           'Non posso devo pulire casa', 'aaaaaaaaaaaa ok']


class InlineHandler(telepot.helper.InlineUserHandler, telepot.helper.AnswererMixin):
    def __init__(self, *args, **kwargs):
        super(InlineHandler, self).__init__(*args, **kwargs)

    def get_definition(self):
        return random.choice(foo)

    def on_inline_query(self, msg):
        def compute_answer():
            query_id, from_id, query_string = telepot.glance(msg, flavor='inline_query')
            if query_string == "random":
                print(self.id, ':', 'Inline Query:', query_id, from_id, query_string)
                articles = [{'type': 'article',
                             'id': 'abc', 'title': query_string, 'message_text': self.get_definition()}]
            else:
                articles = [{'type': 'article',
                             'id': 'abc', 'title': 'error', 'message_text': 'Uaglio non ti capisco'}]
            return articles

        self.answerer.answer(msg, compute_answer)

    def on_chosen_inline_result(self, msg):
        from pprint import pprint
        pprint(msg)
        result_id, from_id, query_string = telepot.glance(msg, flavor='chosen_inline_result')
        print(self.id, ':', 'Chosen Inline Result:', result_id, from_id, query_string)


TOKEN = vignolaBotToken.token

bot = telepot.DelegatorBot(TOKEN, [
    pave_event_space()(
        per_inline_from_id(), create_open, InlineHandler, timeout=10),
])
bot.message_loop(run_forever='Listening ...')