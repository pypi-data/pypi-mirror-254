import io
import copy
import requests
import yaml
from .helpers import WrapperList, select
from .UA import Clash


class Proxy:
    """
    Proxy is a class that represents a proxy defined in the Clash YAML configuration. 
    It has properties like name and DICT. The class can be initialized with either 
    a YAML string or a dictionary (YAML representation).
    """

    def __init__(self, DICT: dict = None, YAML: str = None) -> None:
        """
        Initialize the Proxy object with either a dictionary or a YAML string.

        Args:
            DICT (dict, optional): A dictionary representing a proxy. Defaults to None.
            YAML (str, optional): A string representing a proxy in YAML format. Defaults to None.

        Raises:
            ValueError: If both DICT and YAML are None.
        """

        if DICT:
            self.DICT = DICT
        elif YAML:
            soup = yaml.load(YAML.encode("utf-8"), Loader=yaml.Loader)
            if isinstance(soup, list):
                soup = soup[0]
            self.DICT = soup
        else:
            raise ValueError

    @property
    def name(self) -> str:
        """
        Get the name of the proxy.

        Returns:
            str: The name of the proxy.
        """

        return self.DICT["name"]

    @name.setter
    def name(self, name: str) -> None:
        """
        Set the name of the proxy.

        Args:
            name (str): The new name of the proxy.
        """

        if isinstance(self.__container__, ProxyGroup):
            __container__ = self.__container__.__container__
        elif isinstance(self.__container__, Config):
            __container__ = self.__container__
        foregone = self.DICT["name"]
        if not foregone == name:
            self.DICT["name"] = name
            for i in range(len(__container__.ProxyGroups) - 1, -1, -1):
                for j in __container__.ProxyGroups[i].proxies:
                    if j.name == foregone:
                        j.name = name

    def delete(self, globally: bool = False) -> None:
        """
        Delete the proxy from its proxygroup. If globally is True, the proxy is 
        removed from the configuration file.

        Args:
            globally (bool, optional): If True, the proxy is removed from the configuration file. 
            Defaults to False.
        """

        try:
            if isinstance(self.__container__, ProxyGroup):
                self.__container__.proxies.remove(self)
            elif isinstance(self.__container__, Config):
                globally = True
        except:
            pass
        if globally:
            try:
                if isinstance(self.__container__, ProxyGroup):
                    __container__ = self.__container__.__container__
                elif isinstance(self.__container__, Config):
                    __container__ = self.__container__
                for i in range(len(__container__.ProxyGroups) - 1, -1, -1):
                    for j in range(len(__container__.ProxyGroups[i].proxies) - 1, -1, -1):
                        if __container__.ProxyGroups[i].proxies[j].name == self.name:
                            __container__.ProxyGroups[i].proxies.pop(j)
                for i in range(len(__container__.Proxies) - 1, -1, -1):
                    if __container__.Proxies[i].name == self.name:
                        __container__.Proxies.pop(i)
            except:
                pass

    def __repr__(self) -> str:
        """
        Get a string representation of the proxy.

        Returns:
            str: A string representation of the proxy.
        """

        return f"<PreProcessor.Proxy object {self.name} at {hex(id(self))}>"

    def BATCH(YAML) -> list:
        """
        Create a list of Proxy objects from a YAML string.

        Args:
            YAML (str): A string representing multiple proxies in YAML format.

        Raises:
            ValueError: If the YAML string does not represent a list of proxies.

        Returns:
            list: A list of Proxy objects.
        """

        soup = yaml.load(YAML.encode("utf-8"), Loader=yaml.Loader)
        if isinstance(soup, list):
            return [Proxy(i) for i in soup]
        else:
            raise ValueError("YAML List Expected")


DIRECT = Proxy(DICT={"name": "DIRECT"})
REJECT = Proxy(DICT={"name": "REJECT"})


class NoAliasDumper(yaml.SafeDumper):
    """
    NoAliasDumper is a YAML dumper that ignores aliases. It inherits from yaml.SafeDumper.

    Args:
        yaml (SafeDumper): A YAML dumper.
    """

    def ignore_aliases(self, data) -> bool:
        return True


class Rule:
    """
    Rule is a class that represents a rule defined in the Clash YAML configuration. It has properties 
    like type, argument, policy, and no_resolve. The class can be initialized with 
    either a YAML string or individual properties.
    """

    def __init__(self, YAML: str = None, type: str = None, argument: str = None, policy: str = None, no_resolve: bool = False) -> None:
        """
        Initialize the Rule object with either a YAML string or individual properties.

        Args:
            YAML (str, optional): A string representing a rule in YAML format. Defaults to None.
            type (str, optional): The type of the rule. Defaults to None. For example, "DOMAIN".
            argument (str, optional): The argument of the rule. Defaults to None. For example, "example.com".
            policy (str, optional): The policy of the rule. Defaults to None. For example, "DIRECT".
            no_resolve (bool, optional): A flag indicating whether the rule should be resolved. 
            Defaults to False.

        Raises:
            ValueError: If both YAML and individual properties are None.
        """

        if (type == None or argument == None or policy == None) and YAML == None:
            raise ValueError
        elif YAML == None:
            self.type = type
            self.argument = argument
            self.policy = policy
            self.no_resolve = no_resolve
        else:
            soup = yaml.load(YAML.encode("utf-8"), Loader=yaml.Loader)
            if isinstance(soup, list):
                soup = soup[0]
            self.YAML = soup

    @property
    def no_resolve(self) -> bool:
        """
        Get the no_resolve property of the rule.

        Returns:
            bool: True if the rule should not be resolved, False otherwise.
        """

        return self.no_resolve

    @no_resolve.setter
    def no_resolve(self, no_resolve: bool) -> None:
        """
        Set the no_resolve property of the rule.

        Args:
            no_resolve (bool): True if the rule should not be resolved, False otherwise.
        """

        if no_resolve:
            self._no_resolve = "no-resolve"
        else:
            self._no_resolve = ""

    @property
    def YAML(self) -> str:
        """
        Get the YAML representation of the rule.

        Returns:
            str: The YAML representation of the rule.
        """

        return ",".join(filter(bool, [self.type, self.argument, self.policy, self._no_resolve]))

    @YAML.setter
    def YAML(self, YAML: str) -> None:
        """
        Set the properties of the rule from a YAML string.

        Args:
            YAML (str): A string representing a rule in YAML format.
        """

        tmp = YAML.split(",")
        if "no-resolve" in tmp:
            self.no_resolve = True
            tmp.remove("no-resolve")
        else:
            self.no_resolve = False

        if len(tmp) == 3:
            self.type = tmp[0]
            self.argument = tmp[1]
            self.policy = tmp[2]
        else:
            self.type = None
            self.argument = tmp[0]
            self.policy = tmp[1]

    def delete(self) -> None:
        """
        Delete the rule.
        """

        try:
            self.__container__.Rules.remove(self)
        except:
            pass

    def __repr__(self) -> str:
        """
        Get a string representation of the rule.

        Returns:
            str: A string representation of the rule.
        """

        return f"<PreProcessor.Rule object {self.YAML} at {hex(id(self))}>"

    def BATCH(YAML: str) -> list:
        """
        Create a list of Rule objects from a YAML string.

        Args:
            YAML (str): A string representing multiple rules in YAML format.

        Raises:
            ValueError: If the YAML string does not represent a list of rules.

        Returns:
            list: A list of Rule objects.
        """

        soup = yaml.load(YAML.encode("utf-8"), Loader=yaml.Loader)
        if isinstance(soup, list):
            return [Rule(i) for i in soup]
        else:
            raise ValueError("YAML List Expected")


class ProxyGroup:
    """
    ProxyGroup is a class that represents a proxygroup defined in the Clash YAML configuration. 
    It has properties like name, proxies, and DICT. The class can be initialized with either 
    a dictionary (YAML representation) or a YAML string.
    """

    def __init__(self, DICT: dict = None, YAML: str = None) -> None:
        """
        Initialize the ProxyGroup with either a dictionary or a YAML string.

        Args:
            DICT (dict, optional): A dictionary representing a proxygroup. Defaults to None.
            YAML (str, optional): A string representing a proxygroup in YAML format. Defaults to None.

        Raises:
            ValueError: If both DICT and YAML are None.
        """

        if DICT:
            self.DICT = DICT
        elif YAML:
            soup = yaml.load(YAML.encode("utf-8"), Loader=yaml.Loader)
            if isinstance(soup, list):
                soup = soup[0]
            self.DICT = soup
        else:
            raise ValueError

    @property
    def proxies(self) -> list[Proxy]:
        """
        Get the list of proxies in the proxygroup.

        Returns:
            list[Proxy]: The list of proxies in the proxygroup.
        """

        return self._proxies

    @proxies.setter
    def proxies(self, proxies: list[Proxy]) -> None:
        """
        Set the list of proxies in the proxygroup.

        Args:
            proxies (list[Proxy]): The new list of proxies for the proxygroup.
        """

        self._proxies = WrapperList(self, proxies)

    @property
    def DICT(self) -> dict:
        """
        Get the dictionary representation of the proxygroup.

        Returns:
            dict: The dictionary representation of the proxygroup.
        """

        self._DICT["proxies"] = [i.name for i in self._proxies]
        return self._DICT

    @DICT.setter
    def DICT(self, DICT: dict) -> None:
        """
        Set the properties of the ProxyGroup from a dictionary.

        Args:
            DICT (dict): A dictionary representing a proxygroup.
        """

        self._DICT = DICT
        self.proxies = [Proxy(DICT={"name": i.name}) if isinstance(
            i, Proxy) else Proxy(DICT={"name": i}) for i in self._DICT["proxies"]]

    @property
    def name(self) -> str:
        """
        Get the name of the proxygroup.

        Returns:
            str: The name of the proxygroup.
        """

        return self._DICT["name"]

    @name.setter
    def name(self, name: str) -> None:
        """
        Set the name of the proxygroup.

        Args:
            name (str): The new name of the proxygroup.
        """

        foregone = self._DICT["name"]
        if not foregone == name:
            self._DICT["name"] = name
            try:
                for i in range(len(self.__container__.ProxyGroups) - 1, -1, -1):
                    for j in self.__container__.ProxyGroups[i].proxies:
                        if j.name == foregone:
                            j.name = name
                for i in self.__container__.Rules:
                    if i.policy == foregone:
                        i.policy = name
            except:
                pass

    def delete(self, policy: str = None) -> None:
        """
        Delete the proxygroup. If a policy is provided, all rules with 
        the proxygroup's name as their policy will be updated to use the provided policy.

        Args:
            policy (str, optional): The new policy for rules that use the proxygroup's name as their policy. 
            Defaults to None.
        """

        if policy == None:
            try:
                for i in range(len(self.__container__.Rules) - 1, -1, -1):
                    if self.__container__.Rules[i].policy == self.name:
                        self.__container__.Rules[i].delete()
            except:
                pass
        else:
            try:
                for i in range(len(self.__container__.Rules)):
                    if self.__container__.Rules[i].policy == self.name:
                        self.__container__.Rules[i].policy = policy
            except:
                pass
        try:
            self.__container__.ProxyGroups.remove(self)
        except:
            pass
        try:
            for i in range(len(self.__container__.ProxyGroups) - 1, -1, -1):
                select(
                    self.__container__.ProxyGroups[i].proxies, False, name=self.name).delete()
        except:
            pass

    def __repr__(self) -> str:
        """
        Get a string representation of the proxygroup.

        Returns:
            str: A string representation of the proxygroup.
        """

        return f"<PreProcessor.ProxyGroup object {self.name} at {hex(id(self))}>"

    def BATCH(YAML: str) -> list:
        """
        Create a list of ProxyGroup objects from a YAML string.

        Args:
            YAML (str): A string representing multiple proxygroups in YAML format.

        Raises:
            ValueError: If the YAML string does not represent a list of proxygroups.

        Returns:
            list: A list of ProxyGroup objects.
        """

        soup = yaml.load(YAML.encode("utf-8"), Loader=yaml.Loader)
        if isinstance(soup, list):
            return [ProxyGroup(i) for i in soup]
        else:
            raise ValueError("YAML List Expected")


class Config:
    """
    Config is a class that represents a Clash YAML configuration.
    It can be initialized with a URL, a YAML string, a file, or a dictionary (YAML representation).
    """

    def __init__(self, Url: str = None, YAML: str = None, File: io.TextIOWrapper = None, DICT: dict = None, UA: str = Clash("1.11.0")) -> None:
        """
        Initialize the Config with a URL, a YAML string, a file, or a dictionary (YAML representation).

        Args:
            Url (str, optional): URL to fetch the configuration from. Defaults to None.
            YAML (str, optional): YAML string representing the configuration. Defaults to None.
            File (io.TextIOWrapper, optional): File containing the configuration. Defaults to None.
            DICT (dict, optional): Dictionary representing the configuration. Defaults to None.
            UA (str, optional): User-agent string for the request. Defaults to Default("1.11.0").

        Raises:
            ValueError: If none of Url, YAML, File, or DICT are provided.
        """

        self._bypass = ("DICT", "Proxies", "ProxyGroups", "Rules", "YAML", "_DICT",
                        "_Proxies", "_ProxyGroups", "_Rules", "_meta", "__container__")
        self._meta = {}
        self._Rules = WrapperList(self)
        self._ProxyGroups = WrapperList(self)
        self._Proxies = WrapperList(self)
        self._DICT = {}
        self._meta["headers"] = {}
        if DICT:
            self.DICT = DICT
        elif Url:
            res = requests.get(Url, headers={"user-agent": UA})
            try:
                self._meta["headers"]["subscription-userinfo"] = res.headers["subscription-userinfo"]
            except:
                pass
            try:
                self._meta["headers"]["profile-update-interval"] = res.headers["profile-update-interval"]
            except:
                pass
            try:
                self._meta["headers"]["profile-web-page-url"] = res.headers["profile-web-page-url"]
            except:
                pass
            self.YAML = res.text
        elif YAML:
            self.YAML = YAML
        elif File:
            self.YAML = File.read()
        else:
            raise ValueError

    def __setattr__(self, __name: str, __value) -> None:
        """
        Rewrite the __setattr__ method to intercept attribute assignments and store them in the _meta dictionary.

        Args:
            __name (str): Name of the attribute.
            __value: Value of the attribute.
        """

        if __name == "_bypass" or __name in self._bypass:
            object.__setattr__(self, __name, __value)
        else:
            self._meta[__name] = __value

    def __getattr__(self, __name: str):
        """
        Get an attribute of the configuration.

        Args:
            __name (str): Name of the attribute.

        Returns:
            The value of the attribute.
        """

        if __name == "_bypass" or __name in self._bypass:
            return object.__getattribute__(self, __name)
        else:
            return self._meta[__name]

    @property
    def Proxies(self) -> list[Proxy]:
        """
        Get all proxies.

        Returns:
            list[Proxy]: List of all proxies.
        """

        return self._Proxies

    @Proxies.setter
    def Proxies(self, Proxies: list[Proxy]) -> None:
        """
        Rewrite the Proxies setter to store the proxies in a WrapperList.

        Returns:
            list[ProxyGroup]: List of Proxy objects.
        """

        self._Proxies = WrapperList(self, Proxies)

    @property
    def ProxyGroups(self) -> list[ProxyGroup]:
        """
        Get all proxygroups.

        Returns:
            list[ProxyGroup]: List of all proxygroups.
        """

        return self._ProxyGroups

    @ProxyGroups.setter
    def ProxyGroups(self, ProxyGroups: list[ProxyGroup]) -> None:
        """
        Rewrite the ProxyGroups setter to store the proxygroups in a WrapperList.

        Args:
            ProxyGroups (list[ProxyGroup]): List of ProxyGroup objects.
        """

        self._ProxyGroups = WrapperList(self, ProxyGroups)

    @property
    def Rules(self) -> list[Rule]:
        """
        Get all rules.

        Returns:
            list[Rule]: List of Rule objects.
        """

        return self._Rules

    @Rules.setter
    def Rules(self, Rules: list[Rule]) -> None:
        """
        Rewrite the Rules setter to store the rules in a WrapperList.

        Args:
            Rules (list[Rule]): List of Rule objects.
        """

        self._Rules = WrapperList(self, Rules)

    def getProxies(self, groups: bool = False, embedded: bool = False) -> list[Proxy]:
        """
        Get all proxies, optionally including proxygroups and embedded proxies.

        Args:
            groups (bool, optional): Whether to include proxygroups. Defaults to False.
            embedded (bool, optional): Whether to include embedded proxies. Defaults to False.

        Returns:
            list[Proxy]: List of Proxy objects.
        """

        result = self.Proxies
        if groups:
            result += [
                Proxy(DICT={"name": i.name})
                for i in self.ProxyGroups
            ]
        if embedded:
            result += [
                DIRECT,
                REJECT
            ]
        return result

    def mixin(self, YAML: str = None, DICT: dict = None) -> None:
        """
        Mix additional configuration from a YAML string or a dictionary.

        Args:
            YAML (str, optional): YAML string representing additional configuration. Defaults to None.
            DICT (dict, optional): Dictionary representing additional configuration. Defaults to None.

        Raises:
            ValueError: If neither YAML nor DICT is provided.
        """

        if DICT:
            YAML = yaml.dump(self.DICT, Dumper=NoAliasDumper)
        elif YAML:
            pass
        else:
            raise ValueError()
        self.YAML = self.YAML + "\n" + YAML

    @property
    def DICT(self) -> dict:
        """
        Get the dictionary representation of the configuration.

        Returns:
            dict: Dictionary representation of the configuration.
        """

        self._DICT["proxies"] = [i.DICT for i in self.Proxies]
        self._DICT["proxy-groups"] = [i.DICT for i in self.ProxyGroups]
        self._DICT["rules"] = [i.YAML for i in self.Rules]
        return self._DICT

    @DICT.setter
    def DICT(self, DICT: dict) -> None:
        """
        Set the configuration from a dictionary representation.

        Args:
            DICT (dict): Dictionary representing the configuration.
        """

        self._DICT = DICT
        for i in self._DICT["proxy-groups"]:
            self.ProxyGroups.append(ProxyGroup(DICT=i))
        for i in self._DICT["proxies"]:
            self.Proxies.append(Proxy(DICT=i))
        for i in self._DICT["rules"]:
            self.Rules.append(Rule(YAML=i))

    @property
    def YAML(self) -> str:
        """
        Get the YAML representation of the configuration.

        Returns:
            str: YAML representation of the configuration.
        """

        return yaml.dump(self.DICT, Dumper=NoAliasDumper)

    @YAML.setter
    def YAML(self, YAML: str) -> None:
        """
        Set the configuration from a YAML string.

        Args:
            YAML (str): YAML configuration string.
        """

        self.DICT = yaml.load(YAML.encode("utf-8"), Loader=yaml.Loader)

    def strip(self) -> None:
        """
        Remove any empty proxygroup.
        """

        for i in self.ProxyGroups:
            if len(i.proxies) == 0:
                i.delete()


def deepcopy(config: Config) -> Config:
    """
    Create a deep copy of a Config object.

    Args:
        config (Config): The Config object to be copied.

    Returns:
        Config: The deep copy of a Config object.
    """

    r = Config(DICT=copy.deepcopy(config.DICT))
    r._meta = copy.deepcopy(config._meta)
    return r
