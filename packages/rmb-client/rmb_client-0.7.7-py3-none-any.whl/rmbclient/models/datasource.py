from rmbcommon.models import DataSourceCore, MetaData
from rmbclient.models.base import convert_to_object, BaseResourceList
from rmbcommon.exceptions.client import DataSourceNotFound


class MetaDataClientModel:
    def __init__(self, api, datasource_id):
        self.api = api
        self.datasource_id = datasource_id

    def get(self, from_where="in_brain"):
        if from_where not in ["runtime", "in_brain"]:
            raise ValueError("from_where must be one of runtime/in_brain")
        return MetaData.load_from_dict(
            self.api.send(
                endpoint=f"/datasources/{self.datasource_id}/meta",
                method="GET",
                params={"from_where": from_where}
            )
        )

    def get_runtime(self):
        return self.get(from_where="runtime")

    def sync(self):
        return self.api.send(endpoint=f"/datasources/{self.datasource_id}/meta", method="POST")


class DataSourceClientModel(DataSourceCore):

    @property
    def meta(self) -> MetaDataClientModel:
        return MetaDataClientModel(self.api, self.id)

    def delete(self):
        return self.api.send(endpoint=f"/datasources/{self.id}", method="DELETE")


class DataResourceList(BaseResourceList):
    __do_not_print_properties__ = ['access_config']

    @convert_to_object(cls=DataSourceClientModel)
    def _get_all_resources(self):
        # 获取所有资源
        datasources = self.api.send(endpoint=self.endpoint, method="GET")
        return datasources

    @convert_to_object(cls=DataSourceClientModel)
    def get(self, id=None, name=None):
        if name:
            ds_list = self.api.send(endpoint=f"{self.endpoint}?name={name}", method="GET")
            if ds_list:
                return ds_list
            else:
                raise DataSourceNotFound(f"Data Source {name} not found")

        if not id:
            raise ValueError("No ID or Name provided")
        # 通过资源ID来获取
        return self.api.send(endpoint=f"{self.endpoint}{id}", method="GET")

    @convert_to_object(cls=DataSourceClientModel)
    def register(self, ds_type, ds_access_config, ds_name=None):
        data = {
            "type": ds_type, "name": ds_name,
            "access_config": ds_access_config
        }
        return self.api.send(endpoint=self.endpoint, method="POST", data=data)





