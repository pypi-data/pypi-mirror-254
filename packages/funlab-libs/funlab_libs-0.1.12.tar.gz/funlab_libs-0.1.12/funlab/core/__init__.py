import copy
from dataclasses import is_dataclass
import dataclasses
from datetime import date, datetime, time, timedelta
import inspect
import json
from pathlib import Path
from funlab.utils import dtts, config

class _Readable:
    # __extra_readattr: dict[str, str] = field(init=False, repr=False, default=None)
    # def add_extra_readattr(self, attr_name:str, attr_type:str):
    #     getattr(self, attr_name)  # check if not found, will raise AttributeError
    #     if getattr(self, '_Readable__extra_readattr', None) is None:
    #         self.__extra_readattr = {}
    #     self.__extra_readattr.update({attr_name: attr_type})

    def __to_readable__(self, attr_name:str, attr_type:str|type):
        if isinstance(attr_type, type):
            attr_type = str(attr_type)
            c, n, *_ = str(type(attr_type)).split("'")
            if c.endswith('class'):
                attr_type = n
            else:
                *_, attr_type = c.strip().split('<')

        if attr_name == 'timestamp' or attr_name.endswith('_ts'):
            val = getattr(self, attr_name)
            val:datetime = dtts.utc_timestamp2local_datetime(val) #datetime.fromtimestamp(val).replace(tzinfo=timezone.utc).astimezone(tz=LOCAL_TZ).strftime('%Y-%m-%d %H:%M:%S') if val else ''
            if isinstance(val, datetime) and val - datetime.combine(val.date(), time(0, 0, 0)) == timedelta(0):
                val = val.date()
            val = val.isoformat()
        elif attr_type in ('datetime', 'date') :
            val = getattr(self, attr_name).isoformat()
        elif attr_type == 'float':
            val = float(getattr(self, attr_name))
            if attr_name.endswith('_rate') or attr_name.endswith('_ratio'):
                val = f'{val:.2%}'
            elif int(val) == getattr(self, attr_name):
                val = f'{val:.0f}'
            else:
                val = f'{getattr(self, attr_name):.2f}'
        elif attr_type == 'int':
            val = f'{int(getattr(self, attr_name)):d}'
        elif attr_type == 'enum':
            val = getattr(self, attr_name)
            val = f'{val.name}'
        elif attr_name=='password' or attr_name=='passwd':
            val = '***'
        else:
            val = getattr(self, attr_name)
        return {attr_name: val}

    def __readattrs__(self)-> dict:
        attrs = {}
        fields = dataclasses.fields(self)
        for field in fields:
            if field.init:
                attrs.update(self.__to_readable__(field.name, field.type))
        # try:
        #     extra_readattr = self.__extra_readattr.items()
        # except:
        #     extra_readattr = {}

        # for attr_name, attr_type in extra_readattr:
        #     attrs.update(self.__to_readable__(attr_name, attr_type))

        property_names=[p for p in dir(self) if isinstance(getattr(self,p),property)]

        for prop in property_names:
            prop_type = type(getattr(self, prop))
            attrs.update(self.__to_readable__(prop, prop_type))
        return attrs

    # def __repr__(self):
    #     return f'{self.__readattrs__()}'  #self.to_json()}'

    def __str__(self):
        return f'{self.__class__.__name__}{self.__readattrs__()}'

    def to_json(self) -> str:
        return json.dumps(self, cls=DataclassJSONEncoder)

    # def to_dict(self)->dict:
    #     pass

class DataclassJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if is_dataclass(o):
            if isinstance(o, _Readable):
                return o.__readattrs__()
            else:
                attrs = {}
                for field in dataclasses.fields(self):
                    if field.repr:
                        if field.name == 'timestamp' or field.name.endswith('_ts'):
                            val = getattr(self, field.name)
                            val:datetime = dtts.utc_timestamp2local_datetime(val) #datetime.fromtimestamp(val).replace(tzinfo=timezone.utc).astimezone(tz=LOCAL_TZ).strftime('%Y-%m-%d %H:%M:%S') if val else ''
                            if isinstance(val, datetime) and val - datetime.combine(val.date(), time(0, 0, 0)) == timedelta(0):
                                val = val.date()
                            val = val.isoformat()
                        elif field.type in (datetime, date) :
                            val = getattr(self, field.name).isoformat()
                        else:
                            val = getattr(self, field.name)
                        attrs[field.name] = val
                return f'{attrs}'
        elif type(o) in (datetime, date) :
            return o.isoformat()
        return super().default(o)

class _Configuable:

    def get_config(self, file_name:str, group_section=None, ext_config:config.Config=None, case_insensitive=False) -> config.Config:
        root = Path(inspect.getmodule(self).__file__).parent
        conf_file = root.joinpath(f'conf/{file_name}')
        if conf_file.exists():
            my_conf = config.Config(conf_file, env_file_or_values=ext_config._env_vars if ext_config else {}
                                    , case_insensitive=case_insensitive)
        else:
            my_conf = config.Config({})

        if not group_section:
            group_section = self.__class__.__name__

        if ext_config:
            ext_config.update_with_default(default_conf=my_conf, section=group_section)
            my_conf = ext_config.get_subsection_config(group_section if group_section else self.__class__.__name__
                                                        , default=config.Config({}, case_insensitive=case_insensitive), case_insensitive=case_insensitive)
            return my_conf

class _Extendable:
    """

    """
    def __init__(self) -> None:
        self._extra_data = {}

    def __copy__(self):
        cls = self.__class__
        result = cls.__new__(cls)
        result.__dict__.update(self.__dict__)
        return result

    def __deepcopy__(self, memo):
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        for k, v in self.__dict__.items():
            setattr(result, k, copy.deepcopy(v, memo))
        return result

    def __getattr__(self, key):
        if key in self._extra_data:
            val = self._extra_data[key]
            return val
        return super().__getattribute__(key)

    def set_attr(self, attr, value):
        self._extra_data[attr] = value
