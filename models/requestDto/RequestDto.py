from string import Formatter


class RequestDto:
    method = "GET"
    endpoint = ""

    def __init__(self):
        pass

    def get_path_params(self):
        """
        Obtiene automáticamente los parámetros que aparecen
        como {param} dentro del endpoint.
        """
        formatter = Formatter()

        path_params = {}

        for _, field_name, _, _ in formatter.parse(self.endpoint):
            if field_name is not None:
                path_params[field_name] = getattr(self, field_name, None)

        return path_params

    def get_query_params(self):
        """
        Obtiene todos los atributos que NO forman parte del path.
        Los None se eliminan.
        """
        path_fields = set(self.get_path_params().keys())

        query_params = {}

        for key, value in self.__dict__.items():

            if key in path_fields:
                continue

            if value is None:
                continue

            # Los filtros dinámicos de Megafilter
            if key == "filters":
                query_params.update(value)
                continue

            # CoinGecko normalmente utiliza valores separados por coma
            if isinstance(value, (list, tuple, set)):
                value = ",".join(map(str, value))

            query_params[key] = value

        return query_params

    def get_url(self, base_url):
        path_params = self.get_path_params()

        endpoint = self.endpoint.format(**path_params)

        return f"{base_url.rstrip('/')}/{endpoint.lstrip('/')}"
