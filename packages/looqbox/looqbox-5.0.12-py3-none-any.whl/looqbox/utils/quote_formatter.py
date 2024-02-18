class QuoteFormatter:
    def __init__(self, text):
        self.text = text
        self.quotes = ["'", '"']
        self.separators = [":", ",", ";"]

    def _remove_backslashes(self):
        self.text = self.text.replace("\\", "")

    def _get_char_positions(self):
        positions = []
        for idx, char in enumerate(self.text):
            if char in self.quotes or char in self.separators:
                positions.append((idx, char))
        return positions

    def _get_quotes_to_escape(self, char_positions):
        to_escape = set()
        for i in range(1, len(char_positions) - 1):
            if self._is_quote_between_quotes(char_positions, i):
                to_escape.add(char_positions[i][0])
        return to_escape

    def _is_quote_between_quotes(self, char_positions, i):
        return (char_positions[i][1] in self.quotes and
                char_positions[i - 1][1] in self.quotes and
                char_positions[i + 1][1] in self.quotes)

    def _construct_escaped_text(self, to_escape):
        result = []
        for idx, char in enumerate(self.text):
            if idx in to_escape:
                result.append("\\")
            result.append(char)
        return ''.join(result)

    def format_quotes(self):
        self._remove_backslashes()
        char_positions = self._get_char_positions()
        to_escape = self._get_quotes_to_escape(char_positions)
        return self._construct_escaped_text(to_escape)
