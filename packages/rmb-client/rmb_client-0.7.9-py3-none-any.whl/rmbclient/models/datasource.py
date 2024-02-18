from rmbcommon.models import DataSourceCore, MetaData
from rmbclient.models.base import convert_to_object, BaseResourceList
from rmbcommon.exceptions.client import DataSourceNotFound


class MetaDataClientModel(MetaData):

    def sync(self):
        return self.api.send(endpoint=f"/datasources/{self.datasource_id}/meta", method="POST")


class DataSourceClientModel(DataSourceCore):

    @property
    @convert_to_object(cls=MetaDataClientModel)
    def meta(self):
        return self.api.send(endpoint=f"/datasources/{self.id}/meta", method="GET")

    @property
    @convert_to_object(cls=MetaDataClientModel)
    def meta_runtime(self):
        return self.api.send(
            endpoint=f"/datasources/{self.id}/meta",
            method="GET",
            params={"from_where": "runtime"}
        )

    def delete(self):
        return self.api.send(endpoint=f"/datasources/{self.id}", method="DELETE")


class DataResourceList(BaseResourceList):
    __do_not_print_properties__ = ['tenant_id', 'access_config']

    @convert_to_object(cls=DataSourceClientModel)
    def _get_all_resources(self):
        return self._get_all_resources_request()

    def _get_all_resources_request(self):
        # 获取所有资源
        datasources = self.api.send(endpoint=self.endpoint, method="GET")
        return datasources

    @property
    @convert_to_object(cls=DataSourceClientModel)
    def last(self):
        # 获取最后一个资源
        return self._get_all_resources_request()[-1]

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





