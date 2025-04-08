def d4j_path_prefix(proj, bug_num):
    bug_num = int(bug_num)
    if proj == 'Chart':
        return 'source/'
    elif proj == 'Closure':
        return 'src/'
    elif proj == 'Lang':
        if bug_num <= 35:
            return 'src/main/java/'
        else:
            return 'src/java/'
    elif proj == 'Math':
        if bug_num <= 84:
            return 'src/main/java/'
        else:
            return 'src/java/'
    elif proj == 'Mockito':
        return 'src/'
    elif proj == 'Time':
        return 'src/main/java/'
    elif proj == 'Cli':
        if bug_num <= 29:
            return 'src/java/'
        else:
            return 'src/main/java/'
    elif proj == 'Codec':
        if bug_num <= 10:
            return 'src/java/'
        else:
            return 'src/main/java/'
    elif proj == 'Collections':
        return 'src/main/java/'
    elif proj == 'Compress':
        return 'src/main/java/'
    elif proj == 'Csv':
        return 'src/main/java/'
    elif proj == 'Gson':
        return 'gson/src/main/java/'
    elif proj in ('JacksonCore', 'JacksonDatabind', 'JacksonXml'):
        return 'src/main/java/'
    elif proj == 'Jsoup':
        return 'src/main/java/'
    elif proj == 'JxPath':
        return 'src/java/'
    else:
        raise ValueError(f'Unrecognized project {proj}')

class GTInfo:
    def __init__(self, bugid, filepath: str, method: str, line_range: list, FIB: list):
        prefix = d4j_path_prefix(bugid.split('_')[0],bugid.split('_')[1])
        self.source_file = filepath.split(prefix)[1].split('.java')[0].replace('/','.')
        self.start_line = line_range[0]
        self.end_line = line_range[1]
        self.method = method
        self.bug_id = bugid

    def __repr__(self):
        return str({
            "source_file": self.source_file,
            "start_line": self.start_line,
            "end_line": self.end_line,
            "method": self.method
        })


class Method:
    def __init__(self, File: str, Signature: str, StartLine: str, EndLine: str, Suspiciousness: str, method: str):
        self.file = File
        self.signature = Signature
        self.start_line = int(StartLine)
        self.end_line = int(EndLine)
        self.score = float(Suspiciousness)
        self.method = method

    def __repr__(self):
        return str({
            "File": self.file,
            "Signature": self.signature,
            "StartLine": self.start_line,
            "EndLine": self.end_line,
            "Suspiciousness": self.score
        })

    def cover(self, gt: GTInfo):
        # print(self, gt)
        if self.file == gt.source_file:
            if gt.start_line == self.start_line and gt.end_line == self.end_line and self.method == 'irfl':
                return True
            if gt.start_line <= self.start_line and gt.end_line >= self.end_line and self.method == 'stat2func':
                return True
        return False