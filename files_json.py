import json
import estilo as es

class JsonFile:

    def create_ResultadosJSON(texto, title_operaciones, operaciones, expre, estilo):

        data = {
            "title": title_operaciones,
            "description": texto,
            "operaciones": []
        }

        for num, op in zip(operaciones, expre):
            data["operaciones"].append({
                "numero": num,
                "expresion": op
            })

        json.dump(data, open("jsons/RESULTADOS_202100081.json", 'w'))

    def create_ErroresJSON(errores):

        data = {
            "errores": []
        }

        for error in errores:
            data["errores"].append({
                "lexema": error[0],
                "tipo": error[1],
                "fila": error[2],
                "columna": error[3]
            })

        json.dump(data, open("jsons/ERRORES_202100081", 'w'))

