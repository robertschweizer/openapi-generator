# coding: utf-8

# flake8: noqa
"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from petstore_client_aiohttp.models.additional_properties_any_type import AdditionalPropertiesAnyType
from petstore_client_aiohttp.models.additional_properties_class import AdditionalPropertiesClass
from petstore_client_aiohttp.models.additional_properties_object import AdditionalPropertiesObject
from petstore_client_aiohttp.models.additional_properties_with_description_only import AdditionalPropertiesWithDescriptionOnly
from petstore_client_aiohttp.models.all_of_with_single_ref import AllOfWithSingleRef
from petstore_client_aiohttp.models.animal import Animal
from petstore_client_aiohttp.models.any_of_color import AnyOfColor
from petstore_client_aiohttp.models.any_of_pig import AnyOfPig
from petstore_client_aiohttp.models.api_response import ApiResponse
from petstore_client_aiohttp.models.array_of_array_of_model import ArrayOfArrayOfModel
from petstore_client_aiohttp.models.array_of_array_of_number_only import ArrayOfArrayOfNumberOnly
from petstore_client_aiohttp.models.array_of_number_only import ArrayOfNumberOnly
from petstore_client_aiohttp.models.array_test import ArrayTest
from petstore_client_aiohttp.models.basque_pig import BasquePig
from petstore_client_aiohttp.models.capitalization import Capitalization
from petstore_client_aiohttp.models.cat import Cat
from petstore_client_aiohttp.models.category import Category
from petstore_client_aiohttp.models.circular_reference_model import CircularReferenceModel
from petstore_client_aiohttp.models.class_model import ClassModel
from petstore_client_aiohttp.models.client import Client
from petstore_client_aiohttp.models.color import Color
from petstore_client_aiohttp.models.creature import Creature
from petstore_client_aiohttp.models.creature_info import CreatureInfo
from petstore_client_aiohttp.models.danish_pig import DanishPig
from petstore_client_aiohttp.models.deprecated_object import DeprecatedObject
from petstore_client_aiohttp.models.dog import Dog
from petstore_client_aiohttp.models.dummy_model import DummyModel
from petstore_client_aiohttp.models.enum_arrays import EnumArrays
from petstore_client_aiohttp.models.enum_class import EnumClass
from petstore_client_aiohttp.models.enum_string1 import EnumString1
from petstore_client_aiohttp.models.enum_string2 import EnumString2
from petstore_client_aiohttp.models.enum_test import EnumTest
from petstore_client_aiohttp.models.file import File
from petstore_client_aiohttp.models.file_schema_test_class import FileSchemaTestClass
from petstore_client_aiohttp.models.first_ref import FirstRef
from petstore_client_aiohttp.models.foo import Foo
from petstore_client_aiohttp.models.foo_get_default_response import FooGetDefaultResponse
from petstore_client_aiohttp.models.format_test import FormatTest
from petstore_client_aiohttp.models.has_only_read_only import HasOnlyReadOnly
from petstore_client_aiohttp.models.health_check_result import HealthCheckResult
from petstore_client_aiohttp.models.inner_dict_with_property import InnerDictWithProperty
from petstore_client_aiohttp.models.int_or_string import IntOrString
from petstore_client_aiohttp.models.list_class import ListClass
from petstore_client_aiohttp.models.map_of_array_of_model import MapOfArrayOfModel
from petstore_client_aiohttp.models.map_test import MapTest
from petstore_client_aiohttp.models.mixed_properties_and_additional_properties_class import MixedPropertiesAndAdditionalPropertiesClass
from petstore_client_aiohttp.models.model200_response import Model200Response
from petstore_client_aiohttp.models.model_return import ModelReturn
from petstore_client_aiohttp.models.name import Name
from petstore_client_aiohttp.models.nullable_class import NullableClass
from petstore_client_aiohttp.models.nullable_property import NullableProperty
from petstore_client_aiohttp.models.number_only import NumberOnly
from petstore_client_aiohttp.models.object_to_test_additional_properties import ObjectToTestAdditionalProperties
from petstore_client_aiohttp.models.object_with_deprecated_fields import ObjectWithDeprecatedFields
from petstore_client_aiohttp.models.one_of_enum_string import OneOfEnumString
from petstore_client_aiohttp.models.order import Order
from petstore_client_aiohttp.models.outer_composite import OuterComposite
from petstore_client_aiohttp.models.outer_enum import OuterEnum
from petstore_client_aiohttp.models.outer_enum_default_value import OuterEnumDefaultValue
from petstore_client_aiohttp.models.outer_enum_integer import OuterEnumInteger
from petstore_client_aiohttp.models.outer_enum_integer_default_value import OuterEnumIntegerDefaultValue
from petstore_client_aiohttp.models.outer_object_with_enum_property import OuterObjectWithEnumProperty
from petstore_client_aiohttp.models.parent import Parent
from petstore_client_aiohttp.models.parent_with_optional_dict import ParentWithOptionalDict
from petstore_client_aiohttp.models.pet import Pet
from petstore_client_aiohttp.models.pig import Pig
from petstore_client_aiohttp.models.property_name_collision import PropertyNameCollision
from petstore_client_aiohttp.models.read_only_first import ReadOnlyFirst
from petstore_client_aiohttp.models.second_ref import SecondRef
from petstore_client_aiohttp.models.self_reference_model import SelfReferenceModel
from petstore_client_aiohttp.models.single_ref_type import SingleRefType
from petstore_client_aiohttp.models.special_character_enum import SpecialCharacterEnum
from petstore_client_aiohttp.models.special_model_name import SpecialModelName
from petstore_client_aiohttp.models.special_name import SpecialName
from petstore_client_aiohttp.models.tag import Tag
from petstore_client_aiohttp.models.test_error_responses_with_model400_response import TestErrorResponsesWithModel400Response
from petstore_client_aiohttp.models.test_error_responses_with_model404_response import TestErrorResponsesWithModel404Response
from petstore_client_aiohttp.models.test_inline_freeform_additional_properties_request import TestInlineFreeformAdditionalPropertiesRequest
from petstore_client_aiohttp.models.tiger import Tiger
from petstore_client_aiohttp.models.unnamed_dict_with_additional_model_list_properties import UnnamedDictWithAdditionalModelListProperties
from petstore_client_aiohttp.models.unnamed_dict_with_additional_string_list_properties import UnnamedDictWithAdditionalStringListProperties
from petstore_client_aiohttp.models.user import User
from petstore_client_aiohttp.models.with_nested_one_of import WithNestedOneOf
