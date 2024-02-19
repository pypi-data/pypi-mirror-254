import time


class NanoProfiler:
    def __init__(self, name='default', autostart=False):
        self.name = name
        self._points = []
        self._label_counter = 0

        self._was_started = False

        if autostart:
            self.start()

    def _get_default_label(self):
        self._label_counter += 1
        return 'Label {}'.format(self._label_counter)

    def start(self):
        if self._was_started:
            return

        self._points.append({
            'time': time.time(),
            'label': 'start',
        })
        self._was_started = True

    def mark(self, label=None):
        if not self._was_started:
            raise RuntimeError('Nano profiler was not start')

        self._points.append({
            'time': time.time(),
            'label': label or self.get_default_label()
        })

    def get_stat(self):
        if len(self._points) < 2:
            return []

        it = iter(self._points)
        start = next(it)

        all_time = self._points[-1]['time'] - start['time']

        previous_time = start['time']
        for index, value in enumerate(it, start=1):
            label = value['label']
            diff_time = value['time'] - previous_time
            diff_percentage = round(diff_time / all_time * 100, 2)

            yield (index, diff_time, diff_percentage, label)
            previous_time = value['time']
        yield ('', all_time, 100, 'Total')

    def print_stat(self):
        if not self._was_started:
            return
        stat = self.get_stat()
        self.print_table(stat)

    def print_table(self, stat):
        def _prepare_subitems(items):
            return (' {} '.format(items[0]), ' {:0.3f}s '.format(items[1]),
                    ' {:2.2f}% '.format(items[2]), ' {} '.format(items[3].strip()))

        printable_stat = []
        # max columns content length, without padding
        columns_len = [0] * 4

        # fill columns_len to find max content length of columns
        for items in stat:
            subitems = _prepare_subitems(items)
            printable_stat.append(subitems)
            for index, subitem in enumerate(subitems):
                columns_len[index] = max(
                    columns_len[index],
                    len(subitem),
                )

        caption = ' Statistic of profiler "{}" '.format(self.name)

        # calc as total len of content + all table symbols
        # get maximun length of lines
        total_line_length = sum(columns_len) + 5
        if len(caption) + 2 > total_line_length:
            total_line_length = len(caption) + 2

        # alignt last column to size in according to max line length
        cl = sum(columns_len) + 5
        if total_line_length - cl > 0:
            columns_len[3] += total_line_length - cl

        # print header
        print('┏' + '━' * (total_line_length - 2) + '┓')
        caption_align_left = (total_line_length - 2 - len(caption)) // 2
        caption_align_right = not bool(caption_align_left % 2) if caption_align_left > 0 else 0
        print('┃' + ' ' * caption_align_left + caption + ' ' * caption_align_right + '┃')
        print('┡' + '━' * (columns_len[0]) + '┯' +
              '━' * (columns_len[1]) + '┯' +
              '━' * (columns_len[2]) + '┯' +
              '━' * (columns_len[3]) + '┦')

        # print main table
        for index, items in enumerate(printable_stat[:-1]):
            new_items = []
            for subindex, item in enumerate(items):
                # prepare string template for formating with dynamic length string
                if subindex != len(items) - 1:
                    aligment = '>'
                else:
                    aligment = '<'
                tmpl = ': {}{}s'.format(aligment, columns_len[subindex])
                new_items.append(('{' + tmpl + '}').format(item))

            print('│' + '│'.join(new_items) + '│')

            if index != len(printable_stat[:-1]) - 1:
                print('├' + '─' * (columns_len[0]) + '┼' +
                      '─' * (columns_len[1]) + '┼' +
                      '─' * (columns_len[2]) + '┼' +
                      '─' * (columns_len[3]) + '┤')

        # print bottom
        print('┢' + '━' * (columns_len[0]) + '╈' +
              '━' * (columns_len[1]) + '╈' +
              '━' * (columns_len[2]) + '╈' +
              '━' * (columns_len[3]) + '┪')
        new_items = []
        for subindex, item in enumerate(printable_stat[-1]):
            if subindex != len(items) - 1:
                aligment = '>'
            else:
                aligment = '<'

            tmpl = ': {}{}s'.format(aligment, columns_len[subindex])
            new_items.append(('{' + tmpl + '}').format(item))
        print('┃' + '┃'.join(new_items) + '┃')
        print('┗' + '━' * (columns_len[0]) + '┻' +
              '━' * (columns_len[1]) + '┻' +
              '━' * (columns_len[2]) + '┻' +
              '━' * (columns_len[3]) + '┛')

    def __del__(self):
        self.print_stat()


# Global scope profiler
if globals().get('nano_profiler', None) is None:
    nano_profiler = NanoProfiler('GLOBAL')
