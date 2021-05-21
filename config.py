import yaml
class Configuration(dict):
    """
    Klasa przygotowana pod możliwość rozszerzenia do innego formatu np Json
    """
    def load_from_file(self,file: "path to configuration yaml"):
        try:
            with open(file,'rb') as f:
                try:
                    self._dict= yaml.safe_load(f)
                    print("Configuration loaded successfuly")
                except yaml.YAMLError as exc:
                    print(exc)
        except:
            print("Caugth exception while reading configurtion file!")
    
    def __getitem__(self, key):
        return self._dict.__getitem__(key)

    def __setitem__(self, key, value):
        return self._dict.__setitem__( key, value)

    def __delitem__(self, key):
        return self._dict.__delitem__(key)

    def __contains__(self, key):
        return self._dict.__contains__(key)
            