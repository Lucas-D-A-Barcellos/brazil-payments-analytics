import requests 
import logging

# Configurações de Logs
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)


#Função base de chamada a API, recebe os parametros de url dinamicamente
def get_data(url: str) -> list:

    try:
        logger.info(f"Consumindo endpoint: {url}")

        response = requests.get(url, timeout=60)

        response.raise_for_status()

        data = response.json()

        records = data.get("value", [])

        logger.info(
            f"Consulta realizada com sucesso. "
            f"Registros retornados: {len(records)}"
        )

        return records

    except requests.exceptions.Timeout:
        logger.error(f"Timeout ao acessar {url}")
        raise

    except requests.exceptions.HTTPError as e:
        logger.error(
            f"Erro HTTP {response.status_code} ao acessar {url}"
        )
        raise

    except requests.exceptions.RequestException as e:
        logger.error(
            f"Erro de comunicação ao acessar {url}: {str(e)}"
        )
        raise

    except Exception:
        logger.exception(
            f"Erro inesperado ao processar resposta de {url}"
        )
        raise

