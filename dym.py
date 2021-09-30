from dataclasses import dataclass
from typing import Union

@dataclass(frozen=True)
class DidYouMean:
    textlist: Union[list]

    def check(self, text: Union[str]) -> Union[str,bool]:
        """
        :text: String
        :return: Boolean or String
        """
        true  = 0
        false = 0
        for teks in self.textlist:
            if len(teks) == len(text):
                for y, z in enumerate(teks):
                    if text[y] == z: true += 1
                    else: false += 1
                if len(text) -1 == true and false == 1:
                    return "Did you mean : %s" % teks
                else:
                    true = 0
                    false = 0
        return False
