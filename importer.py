from typing import List


class PersonalResult:
    position: int
    name: str
    points: int

    def __repr__(self):
        return f"{self.name}, #{self.position}, {self.points} points"


def parse_columns(lines) -> List[PersonalResult]:
    IDX_POS = 0
    IDX_NAME = 1
    IDX_POINTS = 2
    IDX_RECORD = 3
    IDX_PERC1 = 4
    IDX_PERC2 = 5
    IDX_PERC3 = 6
    IDX_LAST_COLUMN = 7

    column_index = 0
    result = []
    pers_res = PersonalResult()
    for line in lines:
        line = line.replace("\n", "")
        if column_index == IDX_POS:
            pers_res.position = line
        elif column_index == IDX_NAME:
            pers_res.name = line
        elif column_index == IDX_POINTS:
            pers_res.points = line
        if column_index == IDX_LAST_COLUMN:
            result.append(pers_res)
            pers_res = PersonalResult()
            column_index = 0
        else:
            column_index += 1

    return result


filename = "2021-11-08"
f = open(f"import_data/{filename}.txt", "r")
lines = f.readlines()
for res in parse_columns(lines):
    print(res)
