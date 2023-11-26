# coding: utf-8

# flake8: noqa

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.0.0"

# import apis into sdk package
from petstore_client.api.another_fake_api import AnotherFakeApi
from petstore_client.api.default_api import DefaultApi
from petstore_client.api.fake_api import FakeApi
from petstore_client.api.fake_classname_tags123_api import FakeClassnameTags123Api
from petstore_client.api.pet_api import PetApi
from petstore_client.api.store_api import StoreApi
from petstore_client.api.user_api import UserApi

# import ApiClient
from petstore_client.api_response import ApiResponse
from petstore_client.api_client import ApiClient
from petstore_client.configuration import Configuration
from petstore_client.exceptions import OpenApiException
from petstore_client.exceptions import ApiTypeError
from petstore_client.exceptions import ApiValueError
from petstore_client.exceptions import ApiKeyError
from petstore_client.exceptions import ApiAttributeError
from petstore_client.exceptions import ApiException
from petstore_client.signing import HttpSigningConfiguration

# import models into sdk package
from petstore_client.models.additional_properties_any_type import AdditionalPropertiesAnyType
from petstore_client.models.additional_properties_class import AdditionalPropertiesClass
from petstore_client.models.additional_properties_object import AdditionalPropertiesObject
from petstore_client.models.additional_properties_with_description_only import AdditionalPropertiesWithDescriptionOnly
from petstore_client.models.all_of_with_single_ref import AllOfWithSingleRef
from petstore_client.models.animal import Animal
from petstore_client.models.any_of_color import AnyOfColor
from petstore_client.models.any_of_pig import AnyOfPig
from petstore_client.models.api_response import ApiResponse
from petstore_client.models.array_of_array_of_model import ArrayOfArrayOfModel
from petstore_client.models.array_of_array_of_number_only import ArrayOfArrayOfNumberOnly
from petstore_client.models.array_of_number_only import ArrayOfNumberOnly
from petstore_client.models.array_test import ArrayTest
from petstore_client.models.basque_pig import BasquePig
from petstore_client.models.capitalization import Capitalization
from petstore_client.models.cat import Cat
from petstore_client.models.category import Category
from petstore_client.models.circular_reference_model import CircularReferenceModel
from petstore_client.models.class_model import ClassModel
from petstore_client.models.client import Client
from petstore_client.models.color import Color
from petstore_client.models.creature import Creature
from petstore_client.models.creature_info import CreatureInfo
from petstore_client.models.danish_pig import DanishPig
from petstore_client.models.deprecated_object import DeprecatedObject
from petstore_client.models.dog import Dog
from petstore_client.models.dummy_model import DummyModel
from petstore_client.models.enum_arrays import EnumArrays
from petstore_client.models.enum_class import EnumClass
from petstore_client.models.enum_string1 import EnumString1
from petstore_client.models.enum_string2 import EnumString2
from petstore_client.models.enum_test import EnumTest
from petstore_client.models.file import File
from petstore_client.models.file_schema_test_class import FileSchemaTestClass
from petstore_client.models.first_ref import FirstRef
from petstore_client.models.foo import Foo
from petstore_client.models.foo_get_default_response import FooGetDefaultResponse
from petstore_client.models.format_test import FormatTest
from petstore_client.models.has_only_read_only import HasOnlyReadOnly
from petstore_client.models.health_check_result import HealthCheckResult
from petstore_client.models.inner_dict_with_property import InnerDictWithProperty
from petstore_client.models.int_or_string import IntOrString
from petstore_client.models.list_class import ListClass
from petstore_client.models.map_of_array_of_model import MapOfArrayOfModel
from petstore_client.models.map_test import MapTest
from petstore_client.models.mixed_properties_and_additional_properties_class import MixedPropertiesAndAdditionalPropertiesClass
from petstore_client.models.model200_response import Model200Response
from petstore_client.models.model_return import ModelReturn
from petstore_client.models.name import Name
from petstore_client.models.nullable_class import NullableClass
from petstore_client.models.nullable_property import NullableProperty
from petstore_client.models.number_only import NumberOnly
from petstore_client.models.object_to_test_additional_properties import ObjectToTestAdditionalProperties
from petstore_client.models.object_with_deprecated_fields import ObjectWithDeprecatedFields
from petstore_client.models.one_of_enum_string import OneOfEnumString
from petstore_client.models.order import Order
from petstore_client.models.outer_composite import OuterComposite
from petstore_client.models.outer_enum import OuterEnum
from petstore_client.models.outer_enum_default_value import OuterEnumDefaultValue
from petstore_client.models.outer_enum_integer import OuterEnumInteger
from petstore_client.models.outer_enum_integer_default_value import OuterEnumIntegerDefaultValue
from petstore_client.models.outer_object_with_enum_property import OuterObjectWithEnumProperty
from petstore_client.models.parent import Parent
from petstore_client.models.parent_with_optional_dict import ParentWithOptionalDict
from petstore_client.models.pet import Pet
from petstore_client.models.pig import Pig
from petstore_client.models.property_name_collision import PropertyNameCollision
from petstore_client.models.read_only_first import ReadOnlyFirst
from petstore_client.models.second_ref import SecondRef
from petstore_client.models.self_reference_model import SelfReferenceModel
from petstore_client.models.single_ref_type import SingleRefType
from petstore_client.models.special_character_enum import SpecialCharacterEnum
from petstore_client.models.special_model_name import SpecialModelName
from petstore_client.models.special_name import SpecialName
from petstore_client.models.tag import Tag
from petstore_client.models.test_error_responses_with_model400_response import TestErrorResponsesWithModel400Response
from petstore_client.models.test_error_responses_with_model404_response import TestErrorResponsesWithModel404Response
from petstore_client.models.test_inline_freeform_additional_properties_request import TestInlineFreeformAdditionalPropertiesRequest
from petstore_client.models.tiger import Tiger
from petstore_client.models.unnamed_dict_with_additional_model_list_properties import UnnamedDictWithAdditionalModelListProperties
from petstore_client.models.unnamed_dict_with_additional_string_list_properties import UnnamedDictWithAdditionalStringListProperties
from petstore_client.models.user import User
from petstore_client.models.with_nested_one_of import WithNestedOneOf
