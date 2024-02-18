from .service.kurangdarilima import KurangDariLima

class Number:

    def isKurangLima(self, angka) -> bool:
        return KurangDariLima.isKuranglima(self, angka)
    