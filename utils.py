import json


def read_json(path):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def print_candidat(candidates):
    """
    Вывод списка кандидатов
    """
    list_cand = ''
    for candidate in candidates:
        list_cand += (f'<pre>Имя кандидата: {candidate["name"]}\n'
                      f'Позиция кандидата: {candidate["position"]}\n'
                      f'Навыки: {candidate["skills"]}<pre>\n')
    return list_cand


def print_candidat_id(candidates, cand_id):
    """
    Вывод кандидата по ID
    """
    for candidate in candidates:
        if candidate['id'] == cand_id:
            return candidate


def candidat_skills(candidates, skill):
    """
    Вывод кандидата по навыкам
    """
    result = []
    for candidate in candidates:
        skills = candidate['skills'].lower().split(', ')
        if skill in skills:
            result.append(candidate)
    return result
