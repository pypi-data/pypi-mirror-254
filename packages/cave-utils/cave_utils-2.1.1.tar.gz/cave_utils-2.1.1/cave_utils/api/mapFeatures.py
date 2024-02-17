"""
Create visualizations for your map, including `arc`s, `node`s, and `geo`s, and customize their appearance.
"""
from cave_utils.api_utils.validator_utils import ApiValidator, CustomKeyValidator
from cave_utils.api_utils.general import props, valueLists, layout
import type_enforced
from pamda import pamda


@type_enforced.Enforcer
class mapFeatures(ApiValidator):
    """
    The map features are located under the path **`mapFeatures`**.
    """

    @staticmethod
    def spec(data: dict = dict(), **kwargs):
        """
        Arguments:

        * **`data`**: `[dict]` = `{}` &rarr; The data to pass to `mapFeatures.data.*`.
        """
        return {"kwargs": kwargs, "accepted_values": {}}

    def __extend_spec__(self, **kwargs):
        data = self.data.get("data", {})
        CustomKeyValidator(
            data=data,
            log=self.log,
            prepend_path=["data"],
            validator=mapFeatures_data_star,
            **kwargs,
        )


@type_enforced.Enforcer
class mapFeatures_data_star(ApiValidator):
    """
    The map features data is located under the path **`mapFeatures.data.*`**.
    """

    @staticmethod
    def spec(
        type: str,
        name: str,
        props: dict,
        data: dict,
        layout: [dict, None] = None,
        geoJson: [dict, None] = None,
        **kwargs,
    ):
        """
        Arguments:

        * **`type`**: `[str]` &rarr; The type of the map feature.
            * **Accepted Values**:
                * `"arc"`: An `arc` layer
                * `"node"`: A `node` layer
                * `"geo"`: A `geo` layer
        * **`name`**: `[str]` &rarr; The name of the map feature.
        * **`props`**: `[dict]` &rarr; The props that will be rendered in the map feature.
            * **See**: `cave_utils.api_utils.general.props`
        * **`data`**: `[dict]` &rarr; The data that will be passed to the props.
            * **See**: `cave_utils.api_utils.general.values`
        * **`layout`**: `[dict]` =`{"type": "grid", "numColumns": "auto", "numRows": "auto"}` &rarr;
            * The layout of the map feature data presented in a map modal.
            * **See**: `cave_utils.api_utils.general.layout`
        * **`geoJson`**: `[dict]` =`{}` &rarr; A dictionary specifying the GeoJSON data to use.
            * **See**: `cave_utils.api.mapFeatures.mapFeatures_data_star_geoJson`
        """
        if type not in ["geo", "arc"]:
            if geoJson is not None:
                kwargs["geoJson"] = None
        return {"kwargs": kwargs, "accepted_values": {"type": ["arc", "node", "geo"]}}

    def __extend_spec__(self, **kwargs):
        props_data = self.data.get("props", {})
        CustomKeyValidator(
            data=props_data,
            log=self.log,
            prepend_path=["props"],
            validator=props,
            **kwargs,
        )
        data_data = self.data.get("data")
        if data_data is not None:
            mapFeatures_data_star_data(
                data=data_data,
                log=self.log,
                prepend_path=["data"],
                # Special Kwargs for passing props_data to valueLists
                props_data=props_data,
                # Special Kwargs for passing type and geoJson to location
                layer_type=self.data.get("type"),
                layer_geoJson=self.data.get("geoJson"),
                **kwargs,
            )
        layout_data = self.data.get("layout")
        if layout_data is not None:
            layout(
                data=layout_data,
                log=self.log,
                prepend_path=["layout"],
                prop_id_list=list(props_data.keys()),
                **kwargs,
            )
        if self.data.get("type") in ["geo", "arc"]:
            geoJson_data = self.data.get("geoJson")
            if geoJson_data is None:
                if self.data.get("type") == "geo":
                    self.__error__(
                        msg=f"geoJson is must be specified for type: {self.data.get('type')}",
                        path=["geoJson"],
                    )
            else:
                mapFeatures_data_star_geoJson(
                    data=geoJson_data,
                    log=self.log,
                    prepend_path=["geoJson"],
                    **kwargs,
                )


@type_enforced.Enforcer
class mapFeatures_data_star_data(ApiValidator):
    """
    The map features data is located under the path **`mapFeatures.data.*.data`**.
    """

    @staticmethod
    def spec(location: dict, valueLists: dict, **kwargs):
        """
        Arguments:

        * **`location`**: `[dict]` &rarr; The location lists of the map feature.
            * **See**: `cave_utils.api.mapFeatures.mapFeatures_data_star_data_location`
        * **`valueLists`**: `[dict]` &rarr; The value lists of the map feature.
            * **See**: `cave_utils.api_utils.general.valueLists`
        """
        return {"kwargs": kwargs, "accepted_values": {}}

    def __extend_spec__(self, **kwargs):
        valueLists_data = self.data.get("valueLists", {})
        valueLists(
            data=valueLists_data,
            log=self.log,
            prepend_path=["valueLists"],
            **kwargs,
        )
        location_data = self.data.get("location", {})
        mapFeatures_data_star_data_location(
            data=location_data,
            log=self.log,
            prepend_path=["location"],
            **kwargs,
        )
        # Validate that all lengths are the same
        lengths = [len(v) for k, v in location_data.items() if k not in ["order", "timeValues"]] + [
            len(v) for k, v in valueLists_data.items() if k not in ["order", "timeValues"]
        ]
        if len(set(lengths)) > 1:
            self.__error__(msg=f"location and valueLists keys must have the same length.", path=[])


@type_enforced.Enforcer
class mapFeatures_data_star_data_location(ApiValidator):
    """
    The map features data is located under the path **`mapFeatures.data.*.data.location`**.
    """

    @staticmethod
    def spec(**kwargs):
        """
        Accepts all arbitrary values.

        The location lists you pass will be validated based on other selections in your API spec.
        """
        # TODO: Add docs here given the extended spec below.
        return {
            "kwargs": {},
            "accepted_values": {},
        }

    def __extend_spec__(self, **kwargs):
        layer_type = kwargs.get("layer_type")
        layer_geoJson = kwargs.get("layer_geoJson")
        passed_keys = list(self.data.keys())
        # TODO Figure out way to handle timeValues and order
        optional_keys = ["timeValues", "order"]
        if layer_type == "geo" or (layer_type == "arc" and layer_geoJson):
            required_keys = ["geoJsonValue"]
        elif layer_type == "arc":
            if "path" in passed_keys:
                required_keys = ["path"]
            else:
                required_keys = ["startLatitude", "startLongitude", "endLatitude", "endLongitude"]
                optional_keys += ["startAltitude", "endAltitude"]
        else:
            required_keys = ["latitude", "longitude"]
            optional_keys += ["altitude"]
        missing_keys = pamda.difference(required_keys, list(self.data.keys()))
        if len(missing_keys) > 0:
            self.__error__(msg=f"Missing required keys: {missing_keys}", path=[])
            return
        for key, value_list in self.data.items():
            if key not in required_keys + optional_keys:
                self.__error__(
                    msg=f"`{key}` is not a valid key for location for layer type `{layer_type}`",
                    path=[],
                )
                continue
            if key in ["timeValues", "order"]:
                continue
            if not isinstance(value_list, list):
                self.__error__(
                    msg=f"`{key}` must be a list but got {type(value_list)} instead.", path=[key]
                )
                continue
            latitudes = None
            longitudes = None
            altitudes = None
            if "latitude" in key.lower():
                acceptable_types = (int, float)
                latitudes = value_list
            elif "longitude" in key.lower():
                acceptable_types = (int, float)
                longitudes = value_list
            elif "altitude" in key.lower():
                acceptable_types = (int, float)
                altitudes = value_list
            elif "path" in key.lower():
                acceptable_types = (list,)
                # TODO: Write a better custom path validator to run here.
                try:
                    longitudes = [y[0] for x in value_list for y in x]
                    latitudes = [y[1] for x in value_list for y in x]
                    try:
                        altitudes = [y[2] for x in value_list for y in x]
                    except:
                        altitudes = None
                except:
                    self.__error__(
                        msg=f"`path` must be a list of lists of lists of length 2 or 3. EG: `[[[0,0],[1,1]],[[2,2],[3,3],[4,4],[5,5]]]`",
                        path=[key],
                    )
                    continue
            else:
                acceptable_types = (str,)
            if not self.__check_type_list__(
                data=value_list, types=acceptable_types, prepend_path=[key]
            ):
                continue
            if latitudes is not None:
                if max(latitudes) > 90 or min(latitudes) < -90:
                    self.__error__(
                        msg=f"`{key}` has a latitude that is greater than 90 or less than -90.",
                        path=[key],
                    )
            if longitudes is not None:
                if max(longitudes) > 180 or min(longitudes) < -180:
                    self.__error__(
                        msg=f"`{key}` has a longitude that is greater than 180 or less than -180.",
                        path=[key],
                    )
            if altitudes is not None:
                if max(altitudes) > 10000 or min(altitudes) < 0:
                    self.__error__(
                        msg=f"`{key}` has an altitude that is greater than 10000 or less than 0",
                        path=[key],
                    )


@type_enforced.Enforcer
class mapFeatures_data_star_geoJson(ApiValidator):
    """
    The map feature GeoJSON data is located under the path **`mapFeatures.data.*.geoJson`**.
    """

    @staticmethod
    def spec(geoJsonLayer: str, geoJsonProp: str, **kwargs):
        """
        Arguments:

        * **`geoJsonLayer`**: `[str]` &rarr; The URL of the GeoJSON layer to use.
        * **`geoJsonProp`**: `[str]` &rarr;
            * The `properties` key (from the object fetched from the `geoJsonLayer` URL) to match with the value at `mapFeatures.data.*.data.location.geoJsonValue.*`.
        """
        return {"kwargs": kwargs, "accepted_values": {}}

    def __extend_spec__(self, **kwargs):
        self.__check_url_valid__(url=self.data.get("geoJsonLayer"), prepend_path=["geoJsonLayer"])
