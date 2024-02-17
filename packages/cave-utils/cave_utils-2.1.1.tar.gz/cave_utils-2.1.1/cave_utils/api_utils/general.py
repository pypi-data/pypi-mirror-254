"""
General API Spec items that are found in multiple places. This is not a key that should be passed as part of your `session_data`.
"""
from pamda import pamda
import type_enforced
from cave_utils.api_utils.validator_utils import ApiValidator, CustomKeyValidator


@type_enforced.Enforcer
class props(ApiValidator):
    @staticmethod
    def spec(
        name: str,
        type: str,
        help: [str, None] = None,
        variant: [str, None] = None,
        display: [bool, None] = None,
        enabled: [bool, None] = None,
        apiCommand: [str, None] = None,
        apiCommandKeys: [list, None] = None,
        options: [dict, None] = None,
        placeholder: [str, None] = None,
        maxValue: [float, int, None] = None,
        minValue: [float, int, None] = None,
        maxRows: [int, None] = None,
        minRows: [int, None] = None,
        rows: [int, None] = None,
        notation: [str, None] = None,
        precision: [int, None] = None,
        notationDisplay: [str, None] = None,
        unit: [str, None] = None,
        views: [list, None] = None,
        legendNotation: [str, None] = None,
        legendPrecision: [int, None] = None,
        legendNotationDisplay: [str, None] = None,
        legendMinLabel: [str, None] = None,
        legendMaxLabel: [str, None] = None,
        icon: [str, None] = None,
        trailingZeros: [bool, None] = None,
        unitPlacement: [str, None] = None,
        locale: [str, None] = None,
        fallbackValue: [str, None] = None,
        draggable: [bool, None] = None,
        allowNone: [bool, None] = None,
        **kwargs,
    ):
        """
        Arguments:

        * **`name`**: `[str]` &rarr; The name of the prop.
        * **`type`**: `[str]` &rarr; The type of the prop.
            * **Accepted Values**:
                * `"head"`: A header for an individual section, containing a `title` and a `help` message
                * `"num"`: A numeric input field
                * `"toggle"`: A switch button to enable or disable a single setting
                * `"button"`: A regular button
                * `"text"`: A text input field
                * `"selector"`: Select options from a set
                * `"date"`: Select a date and/or time
                * `"media"`: View various media formats
        * **`help`**: `[str]` = `None` &rarr; The help text to display.
        * **`display`**: `[bool]` = `None` &rarr; Whether or not the prop will be displayed.
        * **`variant`**: `[str]` = `None` &rarr; The variant of the prop.
            * **Accepted Values**:
                * When **`type`** == `"head"`:
                    * `"column"`: A header for a column of related prop items
                    * `"row"`: A header for a row of related prop items
                    * `"icon"`: Same as `"column"`, accompanied by a related icon.
                    * `"iconRow"`: Same as `"row"`, accompanied by a related icon.
                * When **`type`** == `"text"`:
                    * `"single"`: A single-line text input field
                    * `"textarea"`: A multi-line text input field
                * When **`type`** == `"num"`:
                    * `"field"`: A numeric input field
                    * `"slider"`: A range of values along a bar, from which users may select a single value
                    * `"icon"`: A fixed numerical value presented alongside a corresponding icon.
                    * `"iconCompact"`: Similar to `"icon"`, but designed in a compact format for appropriate rendering within a draggable pad.
                * When **`type`** == `"selector"`:
                    * `"checkbox"`: Select one or more items from a set of checkboxes
                    * `"combobox"`: A dropdown with a search bar that allows users to filter options when typing
                    * `"dropdown"`: Show multiple options that appear when the element is clicked
                    * `"nested"`: Select one or more options from a set of nested checkboxes
                    * `"radio"`: Select one option from a set of mutually exclusive options
                    * `"hradio"`: A set of `"radio"`s placed horizontally
                    * `"hstepper"`: Select a unique option along a horizontal slider
                    * `"vstepper"`: Select a unique option along a vertical slider
                * When **`type`** == `"date"`:
                    * `"date"`: Select a date via a calendar pop-up that appears when the element is clicked (default)
                        * **Note**: Passed as `YYYY-MM-DD`
                    * `"time"`: Select a time via a clock pop-up that appears when the element is clicked
                        * **Note**: Passed as `HH:MM:SS`
                    * `"datetime"`: Select date and time via a pop-up with calendar and clock tabs that appear when the element is clicked
                        * **Note**: Passed as `YYYY-MM-DDTHH:MM:SS`
                * When **`type`** == `"media"`:
                    * `"picture"`: Show a PNG or JPG image
                    * `"video"`: Display a YouTube, Vimeo, or Dailymotion video clip
        * **`enabled`**: `[bool]` = `True` &rarr; Whether or not the prop will be enabled.
            * **Note**: This attribute is applicable to all props except `"head"` props.
        * **`apiCommand`**: `[str]` = `None` &rarr; The name of the API command to trigger.
            * **Note**: If `None`, no `apiCommand` is triggered.
            * **Note**: This attribute is applicable to all props except `"head"` props.
        * **`apiCommandKeys`**: `[list]` = `None` &rarr;
            * The root API keys to pass to your `execute_command` function if an `apiCommand` is provided.
            * **Note**: If `None`, all API keys are passed to your `execute_command`.
            * **Note**: This attribute is applicable to all props except `"head"` props.
        * **`icon`**: `[str]` = `None` &rarr; The icon to use for the prop.
            * **Notes**:
                * It must be a valid icon name from the [react-icons][] bundle, preceded by the abbreviated name of the icon library source.
                * This attribute is applicable exclusively to `"head"` props.
        * **`options`**: `[dict]` = `None` &rarr;
            * **Notes**:
                * Only options provided here are valid for the prop value
                * This attribute is applicable exclusively to `"selector"` props
        * **`placeholder`**: `[str]` = `None` &rarr; The placeholder text to display.
            * **Note**: This attribute is applicable exclusively to `"text"` props.
        * **`maxValue`**: `[float | int]` = `None` &rarr; The maximum value for the prop.
            * **Note**: This attribute is applicable exclusively to `"num"` props.
        * **`minValue`**: `[float | int]` = `None` &rarr; The minimum value for the prop.
            * **Note**: This attribute is applicable exclusively to `"num"` props.
        * **`maxRows`**: `[int]` = `None` &rarr;
            * The maximum number of rows to show for a `"textarea"` variant.
            * **Note**: This attribute is applicable exclusively to `"text"` props.
        * **`minRows`**: `[int]` = `None` &rarr;
            * The minimum number of rows to show for a `"textarea"` variant.
            * **Note**: This attribute is applicable exclusively to `"text"` props.
        * **`rows`**: `[int]` = `None` &rarr;
            * The fixed number of rows to show for a `"textarea"` variant.
            * **Note**: This attribute is applicable exclusively to `"text"` props.
        * **`views`**: `[list]` = `["year", "day", "hours", "minutes"]` &rarr;
            * The available time units for the represented date and/or time.
            * **Accepted Values**:
                * `"year"`: The year view
                * `"month"`: The month view
                * `"day"`: The day view
                * `"hours"`: The hours view
                * `"minutes"`: The minutes view
                * `"seconds"`: The seconds view
            * **Notes**:
                * The views will be presented in the order specified in the `views` array.
                * This attribute is applicable exclusively to `"date"` props.
        * **`locale`**: `[str]` = `None` &rarr;
            * Format numeric values based on language and regional conventions.
            * **Notes**:
                * If left unspecified (i.e., `None`), it will default to `settings.defaults.locale`.
                * This attribute is applicable exclusively to `"num"` props.
            * **See**: [Locale identifier][].
        * **`precision`**: `[int]` = `None` &rarr; The number of decimal places to display.
            * **Notes**:
                * Set the precision to `0` to attach an integer constraint.
                * If left unspecified (i.e., `None`), it will default to `settings.defaults.precision`.
                * This attribute is applicable exclusively to `"num"` props.
        * **`trailingZeros`**: `[bool]` = `None` &rarr; If `True`, trailing zeros will be displayed.
            * **Notes**:
                * This ensures that all precision digits are shown. For example: `1.5` &rarr; `1.500` when precision is `3`.
                * If left unspecified (i.e., `None`), it will default to `settings.defaults.trailingZeros`.
                * This attribute is applicable exclusively to `"num"` props.
        * **`fallbackValue`**: [str] = `None` &rarr; A value to show when the value is missing or invalid.
            * **Notes**:
                * This is only for display purposes as related to number formatting. It does not affect the actual value or any computations.
                    * For example, if the value passed is `None`, the fallback value will be displayed instead.
                * If left unspecified (i.e., `None`), it will default to `settings.defaults.fallbackValue`.
                * This attribute is applicable exclusively to `"num"` props.
        * **`unit`**: `[str]` = `None` &rarr; The unit to use for the prop.
            * **Notes**:
                * If left unspecified (i.e., `None`), it will default to `settings.defaults.unit`.
                * This attribute is applicable exclusively to `"num"` props.
        * **`unitPlacement`**: `[str]` = `None` &rarr; The position of the `unit` symbol relative to the value.
            * **Accepted Values**:
                * `"after"`: The `unit` appears after the value.
                * `"afterWithSpace"`: The `unit` appears after the value, separated by a space.
                * `"before"`: The `unit` appears before the value.
                * `"beforeWithSpace"`: The unit is placed before the value, with a space in between.
            * **Notes**:
                * If left unspecified (i.e., `None`), it will default to `settings.defaults.unitPlacement`.
                * This attribute is applicable exclusively to `"num"` props.
        * **`notation`**: `[int]` = `"standard"` &rarr; The formatting style of a numeric value.
            * **Accepted Values**:
                * `"standard"`: Plain number formatting
                * `"compact"`: Resembles the [metric prefix][] system
                * `"scientific"`: [Scientific notation][]
                * `"engineering"`: [Engineering notation][]
            * **Notes**:
                * If left unspecified (i.e., `None`), it will default to `settings.defaults.notation`.
                * This attribute is applicable exclusively to `"num"` props.
        * **`notationDisplay`**: `[str]` = `"e+"` | `"short"` &rarr; Further customize the formatting within the selected `notation`.
            * **Accepted Values**:
                * `"short"`: Add symbols `K`, `M`, `B`, and `T` (in `"en-US"`) to denote thousands, millions, billions, and trillions, respectively.
                * `"long"`: Present numeric values with the informal suffix words `thousand`, `million`, `billion`, and `trillion` (in `"en-US"`).
                * `"e"`: Exponent symbol in lowercase as per the chosen `locale` identifier
                * `"e+"`: Similar to `"e"`, but with a plus sign for positive exponents.
                * `"E"`: Exponent symbol in uppercase as per the chosen `locale` identifier
                * `"E+"`: Similar to `"E"`, but with a plus sign for positive exponents.
                * `"x10^"`: Formal scientific notation representation
                * `"x10^+"`: Similar to `"x10^"`, with a plus sign for positive exponents.
            * **Notes**:
                * No `notationDisplay` option is provided for a `"standard"` notation
                * The options `"short"` and `"long"` are only provided for the `"compact"` notation
                * The options `"e"`, `"e+"`, `"E"`, `"E+"`, `"x10^"`, and `"x10^+"` are provided for the `"scientific"` and `"engineering"` notations
                * If left unspecified (i.e., `None`), it will default to `settings.defaults.notationDisplay`.
                * This attribute is applicable exclusively to `"num"` props.
        * **`legendPrecision`**: `[int]` = `None` &rarr;
            * The number of decimal places to display in the Map Legend.
            * **Notes**:
                * Set the precision to `0` to attach an integer constraint.
                * If left unspecified (i.e., `None`), it will default to `settings.defaults.legendPrecision`.
                * This attribute is applicable exclusively to `"num"` props.
        * **`legendNotation`**: `[int]` = `"standard"` &rarr; The formatting style of a numeric value.
            * **Accepted Values**:
                * `"standard"`: Plain number formatting
                * `"compact"`: Resembles the [metric prefix][] system
                * `"scientific"`: [Scientific notation][]
                * `"engineering"`: [Engineering notation][]
            * **Notes**:
                * If left unspecified (i.e., `None`), it will default to `settings.defaults.legendNotation`.
                * This attribute is applicable exclusively to `"num"` props.
        * **`legendNotationDisplay`**: `[str]` = `"e+"` | `"short"` &rarr; Further customize the formatting within the selected `legendNotation`.
            * **Accepted Values**:
                * `"short"`: Add symbols `K`, `M`, `B`, and `T` (in `"en-US"`) to denote thousands, millions, billions, and trillions, respectively.
                * `"long"`: Present numeric values with the informal suffix words `thousand`, `million`, `billion`, and `trillion` (in `"en-US"`).
                * `"e"`: Exponent symbol in lowercase as per the chosen `locale` identifier
                * `"e+"`: Similar to `"e"`, but with a plus sign for positive exponents.
                * `"E"`: Exponent symbol in uppercase as per the chosen `locale` identifier
                * `"E+"`: Similar to `"E"`, but with a plus sign for positive exponents.
                * `"x10^"`: Formal scientific notation representation
                * `"x10^+"`: Similar to `"x10^"`, with a plus sign for positive exponents.
            * **Notes**:
                * No `legendNotationDisplay` option is provided for a `"standard"` legend notation
                * The options `"short"` and `"long"` are only provided for the `"compact"` legend notation
                * The options `"e"`, `"e+"`, `"E"`, `"E+"`, `"x10^"`, and `"x10^+"` are provided for the `"scientific"` and `"engineering"` legend notations
                * If left unspecified (i.e., `None`), it will default to `settings.defaults.legendNotationDisplay`.
                * This attribute is applicable exclusively to `"num"` props.
        * **`legendMinLabel`**: `[str]` = `None` &rarr;
            * A custom and descriptive label in the Map Legend used to identify the lowest data point.
            * **Notes**:
                * Takes precedence over other formatting, except when used in a node cluster and the `cave_utils.api.maps.group` attribute is `True`. In this case, the min value within the node cluster is displayed.
                * If left unspecified (i.e., `None`), it will default to `settings.defaults.legendMinLabel`.
                * This attribute is applicable exclusively to `"num"` props.
        * **`legendMaxLabel`**: `[str]` = `None` &rarr;
            * A custom and descriptive label in the Map Legend used to identify the highest data point.
            * **Notes**:
                * Takes precedence over other formatting, except when used in a node cluster and the `cave_utils.api.maps.group` attribute is `True`. In this case, the max value within the node cluster is displayed.
                * If left unspecified (i.e., `None`), it will default to `settings.defaults.legendMaxLabel`.
                * This attribute is applicable exclusively to `"num"` props.
        * **`draggable`**: `[bool]` = `None` &rarr;
            * If `True`, the prop will be rendered within the draggable global outputs pad.
            * **Notes**:
                * The prop's `variant` is enforced to `iconCompact` to accommodate it within the draggable pad.
                * This attribute is applicable exclusively to `"num"` props defined within `cave_utils.api.globalOutputs`.
        * **`allowNone`**: `[bool]` = `False` &rarr;
            * Whether or not to allow `None` as a valid value for the prop. This is primarily used to help when validating `values` and `valueLists`.
            * **Notes**:
                * If `True`, `None` will be a valid value for the prop.
                    * `None` values will be treated differently in the front end
                        * For map display purposes: `None` values will be shown as a different color or ignored.
                            * See `nullColor` in: `/cave_utils/cave_utils/api/maps.html#colorByOptions`
                        * For prop purposes: `None` values will be left blank.
                * If `False`, `None` will not be a valid value for the prop.
                * This attribute is applicable to all props except `"head"` props.


        [metric prefix]: https://en.wikipedia.org/wiki/Metric_prefix
        [Scientific notation]: https://en.wikipedia.org/wiki/Scientific_notation
        [Engineering notation]: https://en.wikipedia.org/wiki/Engineering_notation
        """
        passed_values = {k: v for k, v in locals().items() if (v is not None) and k != "kwargs"}
        required_fields = ["name", "type"]
        optional_fields = ["help", "variant", "display"]
        if type != "head":
            optional_fields += ["enabled", "apiCommand", "apiCommandKeys", "allowNone"]
        if type == "head":
            if variant == "icon" or variant == "iconRow":
                required_fields += ["icon"]
        if type == "text":
            optional_fields += ["minRows", "maxRows", "rows"]
        if type == "num":
            if variant == "slider":
                required_fields += ["maxValue", "minValue"]
            else:
                optional_fields += ["maxValue", "minValue"]
            if variant == "icon" or variant == "iconCompact":
                required_fields += ["icon"]
            optional_fields += [
                "unit",
                "notation",
                "precision",
                "notationDisplay",
                "legendNotation",
                "legendPrecision",
                "legendNotationDisplay",
                "legendMinLabel",
                "legendMaxLabel",
                "trailingZeros",
                "unitPlacement",
                "draggable",
            ]
        if type == "selector":
            required_fields += ["options"]
            optional_fields += ["placeholder"]
        if type == "date":
            optional_fields += ["views"]
        missing_required = pamda.difference(required_fields, list(passed_values.keys()))
        if len(missing_required) > 0:
            raise Exception(f"Missing required fields: {str(missing_required)}")
        for k, v in passed_values.items():
            if k not in required_fields + optional_fields:
                kwargs[k] = v
        return {
            "kwargs": kwargs,
            "accepted_values": {
                "type": ["head", "num", "toggle", "button", "text", "selector", "date", "media"],
                "views": ["year", "month", "day", "hours", "minutes", "seconds"],
                "unitPlacement": ["after", "afterWithSpace", "before", "beforeWithSpace"],
                # TODO: Validate
                # compact: allowed notation displays -> "short", "long"
                # scientific|engineering: allowed notation displays -> "e", "e+", "E", "E+", "x10^", "x10^+"
                # standard: allowed notation displays -> None
                "notation": ["compact", "precision", "scientific", "engineering"],
                "notationDisplay": ["short", "long", "e", "e+", "E", "E+", "x10^", "x10^+"],
                "legendNotation": ["compact", "precision", "scientific", "engineering"],
                "legendNotationDisplay": ["short", "long", "e", "e+", "E", "E+", "x10^", "x10^+"],
                "variant": {
                    "head": ["column", "row", "icon", "iconRow"],
                    "text": ["textarea"],
                    "num": ["field", "slider", "icon", "iconCompact"],
                    "selector": [
                        "dropdown",
                        "checkbox",
                        "radio",
                        "combobox",
                        "hstepper",
                        "vstepper",
                        "hradio",
                        "nested",
                    ],
                    "date": ["date", "time", "datetime"],
                    "media": ["picture", "video"],
                }.get(type, []),
            },
        }

    def __extend_spec__(self, **kwargs):
        if self.data.get("type") == "selector":
            CustomKeyValidator(
                data=self.data.get("options", {}),
                log=self.log,
                prepend_path=["options"],
                validator=props_options,
                variant=self.data.get("variant"),
                **kwargs,
            )


class props_options(ApiValidator):
    @staticmethod
    def spec(name: str, path: [list, None] = None, **kwargs):
        """
        Arguments:

        * **`name`**: `[str]` &rarr; The name of the option.
        * **`path`**: `[list]` = `None` &rarr; The path to an option.
            * **Notes**:
                * If `None`, the option will not be selectable
                * This attribute is applicable exclusively to `"nested"` props
        """
        variant = kwargs.get("variant")
        kwargs = {k: v for k, v in kwargs.items() if k != "variant"}
        if variant == "nested":
            if path is None:
                raise Exception("Must provide a path for nested options")
        return {
            "kwargs": kwargs,
            "accepted_values": {},
        }

    def __extend_spec__(self, **kwargs):
        if kwargs.get("variant") == "nested":
            if not isinstance(self.data.get("path"), list):
                self.__error__(
                    msg="`path` must be specified and a list of strings for nested options"
                )
                return
            self.__check_type_list__(
                data=self.data.get("path", []), types=(str,), prepend_path=["path"]
            )


@type_enforced.Enforcer
class layout(ApiValidator):
    @staticmethod
    def spec(
        type: str,
        numColumns: [str, int, None] = None,
        numRows: [str, int, None] = None,
        data: [dict, None] = None,
        itemId: [str, None] = None,
        column: [int, None] = None,
        row: [int, None] = None,
        **kwargs,
    ):
        """
        Arguments:

        * **`type`**: `[str]` = `None` &rarr; The type of the layout.
            * **Accepted Values**:
                * `"grid"`: A layout element that can contain other layout elements.
                * `"item"`: A layout element where a prop is located.
        * **`numColumns`**: `[str | int]` = `"auto"` &rarr; The number of columns for the grid layout.
            * **Notes**:
                * If `"auto"`, the number of columns will be calculated based on the number of items.
                * This attribute is applicable exclusively to `"grid"` layouts.
        * **`numRows`**: `[str | int]` = `"auto"` &rarr; The number of rows for the grid layout.
            * **Notes**:
                * If `"auto"`, the number of rows will be calculated based on the number of items.
                * This attribute is applicable exclusively to `"grid"` layouts.
        * **`data`**: `[dict]` = `None` &rarr; The data for the layout.
            * **Note**: This attribute is applicable exclusively to `"grid"` layouts.
        * **`itemId`**: `[str]` = `None` &rarr; The id of the prop placed in the layout
            * **Note**: This attribute is applicable exclusively to `"item"` layouts.
        * **`column`**: `[int]` = `None` &rarr; The column in which to place the prop in the current grid.
        * **`row`**: `[int]` = `None` &rarr; The row in which to place the prop in the current grid.
        """
        passed_values = {k: v for k, v in locals().items() if (v is not None) and k != "kwargs"}
        if type == "grid":
            required_fields = ["type", "data"]
            optional_fields = ["numColumns", "numRows", "column", "row"]
        if type == "item":
            required_fields = ["type", "itemId"]
            optional_fields = ["column", "row"]
        missing_required = pamda.difference(required_fields, list(passed_values.keys()))
        if len(missing_required) > 0:
            raise Exception(f"Missing required fields: {str(missing_required)}")
        for k, v in passed_values.items():
            if k not in required_fields + optional_fields:
                kwargs[k] = v
        accepted_values = {
            "type": ["grid", "item"],
        }
        if isinstance(numRows, str):
            accepted_values["numRows"] = ["auto"]
        if isinstance(numColumns, str):
            accepted_values["numColumns"] = ["auto"]
        return {
            "kwargs": kwargs,
            "accepted_values": {
                "type": ["grid", "item"],
            },
        }

    def __extend_spec__(self, **kwargs):
        layout_type = self.data.get("type", None)
        if layout_type == "grid":
            for field, value in self.data.get("data", {}).items():
                layout(data=value, log=self.log, prepend_path=["data", field], **kwargs)
        if layout_type == "item":
            item_id = self.data.get("itemId", None)
            prop_id_list = kwargs.get("prop_id_list", [])
            if item_id not in prop_id_list:
                self.__error__(
                    msg=f"`itemId` ({item_id}) does not match any valid prop ids {prop_id_list}"
                )


@type_enforced.Enforcer
class values(ApiValidator):
    @staticmethod
    def spec(**kwargs):
        """
        Accepts all arbitrary values depending on what you have in your props as part of the API spec.

        The values you pass will be validated against the props in your API spec.
        """
        return {
            "kwargs": {},
            "accepted_values": {},
        }

    def __extend_spec__(self, **kwargs):
        props_data = kwargs.get("props_data", {})
        for prop_key, prop_value in self.data.items():
            prop_spec = props_data.get(prop_key, {})
            if not prop_spec:
                self.__error__(
                    msg=f"`{prop_key}` does not match any valid prop ids {list(props_data.keys())}"
                )
                continue
            prop_type = prop_spec.get("type", None)
            if prop_type == "head":
                self.__error__(
                    msg=f"`{prop_key}` with the prop type of `{prop_type}` can not have an associated value."
                )
                continue
            acceptable_types = {
                "num": (int, float),
                "toggle": (bool,),
                "button": (str,),
                "text": (str,),
                "selector": (list,),
                "date": (str,),
                "media": (str,),
            }.get(prop_type, tuple())
            # Add None to acceptable types if allowed
            if prop_spec.get("allowNone", False):
                acceptable_types += (type(None),)
            # Validate types and continue if invalid
            if not self.__check_type__(prop_value, acceptable_types, prepend_path=[prop_key]):
                continue
            # Continue if the value is None
            if prop_value is None:
                continue
            if prop_type == "num":
                min_value = prop_spec.get("minValue", float("-inf"))
                max_value = prop_spec.get("maxValue", float("inf"))
                if prop_value < min_value or prop_value > max_value:
                    self.__error__(
                        msg=f"`{prop_key}` with the prop type of `{prop_type}` must be between {min_value} and {max_value} as defined by the API spec."
                    )
            elif prop_type == "selector":
                options = list(prop_spec.get("options", {}).keys())
                self.__check_subset_valid__(prop_value, options, prepend_path=[prop_key])
            elif prop_type == "date":
                self.__check_date_valid__(
                    prop_value,
                    date_variant=prop_spec.get("variant", "date"),
                    prepend_path=[prop_key],
                )
            elif prop_type == "media":
                self.__check_url_valid__(prop_value, prepend_path=[prop_key])


@type_enforced.Enforcer
class valueLists(ApiValidator):
    @staticmethod
    def spec(**kwargs):
        """
        Accepts all arbitrary values depending on what you have in your props as part of the API spec.

        The valueLists you pass will be validated against the `props` from your API spec.
        """
        return {
            "kwargs": {},
            "accepted_values": {},
        }

    def __extend_spec__(self, **kwargs):
        props_data = kwargs.get("props_data", {})
        for prop_key, prop_value_list in self.data.items():
            if not isinstance(prop_value_list, list):
                self.__error__(
                    msg=f"`{prop_key}` must be a list of values for valueLists", path=[prop_key]
                )
                continue
            prop_spec = props_data.get(prop_key, {})
            if not prop_spec:
                self.__error__(
                    msg=f"`{prop_key}` does not match any valid prop ids {list(props_data.keys())}"
                )
                continue
            prop_type = prop_spec.get("type", None)
            if prop_type == "head":
                self.__error__(
                    msg=f"`{prop_key}` with the prop type of `{prop_type}` can not have an associated value."
                )
                continue
            acceptable_types = {
                "num": (int, float),
                "toggle": (bool,),
                "button": (str,),
                "text": (str,),
                "selector": (list,),
                "date": (str,),
                "media": (str,),
            }.get(prop_type, tuple())
            # Add None to acceptable types if allowed
            if prop_spec.get("allowNone", False):
                acceptable_types += (type(None),)
            if not self.__check_type_list__(
                data=prop_value_list, types=acceptable_types, prepend_path=[prop_key]
            ):
                continue
            if prop_spec.get("allowNone", False):
                prop_value_list = [v for v in prop_value_list if v is not None]
            if prop_type == "num":
                # Validate minimum is met
                min_value = prop_spec.get("minValue")
                if min_value is not None:
                    prop_value_list_min = min(prop_value_list)
                    if prop_value_list_min < min_value:
                        self.__error__(
                            msg=f"`{prop_key}` has a value that is less than {min_value} as defined by the API spec."
                        )
                # Validate maximum is met
                max_value = prop_spec.get("maxValue")
                if max_value is not None:
                    prop_value_list_max = max(prop_value_list)
                    if prop_value_list_max > max_value:
                        self.__error__(
                            msg=f"`{prop_key}` has a value that is greater than {max_value} as defined by the API spec."
                        )
            elif prop_type == "selector":
                options = list(prop_spec.get("options", {}).keys())
                prop_value_list_set = list(set(pamda.flatten(prop_value_list)))
                self.__check_subset_valid__(prop_value_list_set, options, prepend_path=[prop_key])
            elif prop_type == "head":
                self.__error__(
                    msg=f"`{prop_key}` with the prop type of `{prop_type}` can not have an associated value."
                )
            elif prop_type == "date":
                prop_value_list_set = list(set(prop_value_list))
                date_variant = prop_spec.get("variant", "date")
                for prop_value in prop_value_list:
                    if not self.__check_date_valid__(
                        prop_value, date_variant=date_variant, prepend_path=[prop_key]
                    ):
                        continue
            elif prop_type == "media":
                for prop_value in prop_value_list:
                    if not self.__check_url_valid__(prop_value, prepend_path=[prop_key]):
                        continue
