from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AndroidAppDeliveryData(_message.Message):
    __slots__ = ("downloadSize", "sha1", "downloadUrl", "additionalFile", "downloadAuthCookie", "forwardLocked", "refundTimeout", "serverInitiated", "postInstallRefundWindowMillis", "immediateStartNeeded", "patchData", "encryptionParams", "downloadUrlGzipped", "downloadSizeGzipped", "split", "sha256")
    DOWNLOADSIZE_FIELD_NUMBER: _ClassVar[int]
    SHA1_FIELD_NUMBER: _ClassVar[int]
    DOWNLOADURL_FIELD_NUMBER: _ClassVar[int]
    ADDITIONALFILE_FIELD_NUMBER: _ClassVar[int]
    DOWNLOADAUTHCOOKIE_FIELD_NUMBER: _ClassVar[int]
    FORWARDLOCKED_FIELD_NUMBER: _ClassVar[int]
    REFUNDTIMEOUT_FIELD_NUMBER: _ClassVar[int]
    SERVERINITIATED_FIELD_NUMBER: _ClassVar[int]
    POSTINSTALLREFUNDWINDOWMILLIS_FIELD_NUMBER: _ClassVar[int]
    IMMEDIATESTARTNEEDED_FIELD_NUMBER: _ClassVar[int]
    PATCHDATA_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTIONPARAMS_FIELD_NUMBER: _ClassVar[int]
    DOWNLOADURLGZIPPED_FIELD_NUMBER: _ClassVar[int]
    DOWNLOADSIZEGZIPPED_FIELD_NUMBER: _ClassVar[int]
    SPLIT_FIELD_NUMBER: _ClassVar[int]
    SHA256_FIELD_NUMBER: _ClassVar[int]
    downloadSize: int
    sha1: str
    downloadUrl: str
    additionalFile: _containers.RepeatedCompositeFieldContainer[AppFileMetadata]
    downloadAuthCookie: _containers.RepeatedCompositeFieldContainer[HttpCookie]
    forwardLocked: bool
    refundTimeout: int
    serverInitiated: bool
    postInstallRefundWindowMillis: int
    immediateStartNeeded: bool
    patchData: AndroidAppPatchData
    encryptionParams: EncryptionParams
    downloadUrlGzipped: str
    downloadSizeGzipped: int
    split: _containers.RepeatedCompositeFieldContainer[Split]
    sha256: str
    def __init__(self, downloadSize: _Optional[int] = ..., sha1: _Optional[str] = ..., downloadUrl: _Optional[str] = ..., additionalFile: _Optional[_Iterable[_Union[AppFileMetadata, _Mapping]]] = ..., downloadAuthCookie: _Optional[_Iterable[_Union[HttpCookie, _Mapping]]] = ..., forwardLocked: _Optional[bool] = ..., refundTimeout: _Optional[int] = ..., serverInitiated: _Optional[bool] = ..., postInstallRefundWindowMillis: _Optional[int] = ..., immediateStartNeeded: _Optional[bool] = ..., patchData: _Optional[_Union[AndroidAppPatchData, _Mapping]] = ..., encryptionParams: _Optional[_Union[EncryptionParams, _Mapping]] = ..., downloadUrlGzipped: _Optional[str] = ..., downloadSizeGzipped: _Optional[int] = ..., split: _Optional[_Iterable[_Union[Split, _Mapping]]] = ..., sha256: _Optional[str] = ...) -> None: ...

class Split(_message.Message):
    __slots__ = ("name", "size", "sizeGzipped", "sha1", "downloadUrl", "downloadUrlGzipped", "sha256")
    NAME_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    SIZEGZIPPED_FIELD_NUMBER: _ClassVar[int]
    SHA1_FIELD_NUMBER: _ClassVar[int]
    DOWNLOADURL_FIELD_NUMBER: _ClassVar[int]
    DOWNLOADURLGZIPPED_FIELD_NUMBER: _ClassVar[int]
    SHA256_FIELD_NUMBER: _ClassVar[int]
    name: str
    size: int
    sizeGzipped: int
    sha1: str
    downloadUrl: str
    downloadUrlGzipped: str
    sha256: str
    def __init__(self, name: _Optional[str] = ..., size: _Optional[int] = ..., sizeGzipped: _Optional[int] = ..., sha1: _Optional[str] = ..., downloadUrl: _Optional[str] = ..., downloadUrlGzipped: _Optional[str] = ..., sha256: _Optional[str] = ...) -> None: ...

class AndroidAppPatchData(_message.Message):
    __slots__ = ("baseVersionCode", "baseSha1", "downloadUrl", "patchFormat", "maxPatchSize")
    BASEVERSIONCODE_FIELD_NUMBER: _ClassVar[int]
    BASESHA1_FIELD_NUMBER: _ClassVar[int]
    DOWNLOADURL_FIELD_NUMBER: _ClassVar[int]
    PATCHFORMAT_FIELD_NUMBER: _ClassVar[int]
    MAXPATCHSIZE_FIELD_NUMBER: _ClassVar[int]
    baseVersionCode: int
    baseSha1: str
    downloadUrl: str
    patchFormat: int
    maxPatchSize: int
    def __init__(self, baseVersionCode: _Optional[int] = ..., baseSha1: _Optional[str] = ..., downloadUrl: _Optional[str] = ..., patchFormat: _Optional[int] = ..., maxPatchSize: _Optional[int] = ...) -> None: ...

class AppFileMetadata(_message.Message):
    __slots__ = ("fileType", "versionCode", "size", "downloadUrl", "sizeGzipped", "downloadUrlGzipped", "sha1")
    FILETYPE_FIELD_NUMBER: _ClassVar[int]
    VERSIONCODE_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    DOWNLOADURL_FIELD_NUMBER: _ClassVar[int]
    SIZEGZIPPED_FIELD_NUMBER: _ClassVar[int]
    DOWNLOADURLGZIPPED_FIELD_NUMBER: _ClassVar[int]
    SHA1_FIELD_NUMBER: _ClassVar[int]
    fileType: int
    versionCode: int
    size: int
    downloadUrl: str
    sizeGzipped: int
    downloadUrlGzipped: str
    sha1: str
    def __init__(self, fileType: _Optional[int] = ..., versionCode: _Optional[int] = ..., size: _Optional[int] = ..., downloadUrl: _Optional[str] = ..., sizeGzipped: _Optional[int] = ..., downloadUrlGzipped: _Optional[str] = ..., sha1: _Optional[str] = ...) -> None: ...

class EncryptionParams(_message.Message):
    __slots__ = ("version", "encryptionKey", "hmacKey")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTIONKEY_FIELD_NUMBER: _ClassVar[int]
    HMACKEY_FIELD_NUMBER: _ClassVar[int]
    version: int
    encryptionKey: str
    hmacKey: str
    def __init__(self, version: _Optional[int] = ..., encryptionKey: _Optional[str] = ..., hmacKey: _Optional[str] = ...) -> None: ...

class HttpCookie(_message.Message):
    __slots__ = ("name", "value")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: str
    def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class Address(_message.Message):
    __slots__ = ("name", "addressLine1", "addressLine2", "city", "state", "postalCode", "postalCountry", "dependentLocality", "sortingCode", "languageCode", "phoneNumber", "isReduced", "firstName", "lastName", "email")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ADDRESSLINE1_FIELD_NUMBER: _ClassVar[int]
    ADDRESSLINE2_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    POSTALCODE_FIELD_NUMBER: _ClassVar[int]
    POSTALCOUNTRY_FIELD_NUMBER: _ClassVar[int]
    DEPENDENTLOCALITY_FIELD_NUMBER: _ClassVar[int]
    SORTINGCODE_FIELD_NUMBER: _ClassVar[int]
    LANGUAGECODE_FIELD_NUMBER: _ClassVar[int]
    PHONENUMBER_FIELD_NUMBER: _ClassVar[int]
    ISREDUCED_FIELD_NUMBER: _ClassVar[int]
    FIRSTNAME_FIELD_NUMBER: _ClassVar[int]
    LASTNAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    name: str
    addressLine1: str
    addressLine2: str
    city: str
    state: str
    postalCode: str
    postalCountry: str
    dependentLocality: str
    sortingCode: str
    languageCode: str
    phoneNumber: str
    isReduced: bool
    firstName: str
    lastName: str
    email: str
    def __init__(self, name: _Optional[str] = ..., addressLine1: _Optional[str] = ..., addressLine2: _Optional[str] = ..., city: _Optional[str] = ..., state: _Optional[str] = ..., postalCode: _Optional[str] = ..., postalCountry: _Optional[str] = ..., dependentLocality: _Optional[str] = ..., sortingCode: _Optional[str] = ..., languageCode: _Optional[str] = ..., phoneNumber: _Optional[str] = ..., isReduced: _Optional[bool] = ..., firstName: _Optional[str] = ..., lastName: _Optional[str] = ..., email: _Optional[str] = ...) -> None: ...

class BookAuthor(_message.Message):
    __slots__ = ("name", "deprecatedQuery", "docid")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DEPRECATEDQUERY_FIELD_NUMBER: _ClassVar[int]
    DOCID_FIELD_NUMBER: _ClassVar[int]
    name: str
    deprecatedQuery: str
    docid: Docid
    def __init__(self, name: _Optional[str] = ..., deprecatedQuery: _Optional[str] = ..., docid: _Optional[_Union[Docid, _Mapping]] = ...) -> None: ...

class BookDetails(_message.Message):
    __slots__ = ("subject", "publisher", "publicationDate", "isbn", "numberOfPages", "subtitle", "author", "readerUrl", "downloadEpubUrl", "downloadPdfUrl", "acsEpubTokenUrl", "acsPdfTokenUrl", "epubAvailable", "pdfAvailable", "aboutTheAuthor", "identifier")
    class Identifier(_message.Message):
        __slots__ = ("type", "identifier")
        TYPE_FIELD_NUMBER: _ClassVar[int]
        IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
        type: int
        identifier: str
        def __init__(self, type: _Optional[int] = ..., identifier: _Optional[str] = ...) -> None: ...
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    PUBLISHER_FIELD_NUMBER: _ClassVar[int]
    PUBLICATIONDATE_FIELD_NUMBER: _ClassVar[int]
    ISBN_FIELD_NUMBER: _ClassVar[int]
    NUMBEROFPAGES_FIELD_NUMBER: _ClassVar[int]
    SUBTITLE_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    READERURL_FIELD_NUMBER: _ClassVar[int]
    DOWNLOADEPUBURL_FIELD_NUMBER: _ClassVar[int]
    DOWNLOADPDFURL_FIELD_NUMBER: _ClassVar[int]
    ACSEPUBTOKENURL_FIELD_NUMBER: _ClassVar[int]
    ACSPDFTOKENURL_FIELD_NUMBER: _ClassVar[int]
    EPUBAVAILABLE_FIELD_NUMBER: _ClassVar[int]
    PDFAVAILABLE_FIELD_NUMBER: _ClassVar[int]
    ABOUTTHEAUTHOR_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    subject: _containers.RepeatedCompositeFieldContainer[BookSubject]
    publisher: str
    publicationDate: str
    isbn: str
    numberOfPages: int
    subtitle: str
    author: _containers.RepeatedCompositeFieldContainer[BookAuthor]
    readerUrl: str
    downloadEpubUrl: str
    downloadPdfUrl: str
    acsEpubTokenUrl: str
    acsPdfTokenUrl: str
    epubAvailable: bool
    pdfAvailable: bool
    aboutTheAuthor: str
    identifier: _containers.RepeatedCompositeFieldContainer[BookDetails.Identifier]
    def __init__(self, subject: _Optional[_Iterable[_Union[BookSubject, _Mapping]]] = ..., publisher: _Optional[str] = ..., publicationDate: _Optional[str] = ..., isbn: _Optional[str] = ..., numberOfPages: _Optional[int] = ..., subtitle: _Optional[str] = ..., author: _Optional[_Iterable[_Union[BookAuthor, _Mapping]]] = ..., readerUrl: _Optional[str] = ..., downloadEpubUrl: _Optional[str] = ..., downloadPdfUrl: _Optional[str] = ..., acsEpubTokenUrl: _Optional[str] = ..., acsPdfTokenUrl: _Optional[str] = ..., epubAvailable: _Optional[bool] = ..., pdfAvailable: _Optional[bool] = ..., aboutTheAuthor: _Optional[str] = ..., identifier: _Optional[_Iterable[_Union[BookDetails.Identifier, _Mapping]]] = ...) -> None: ...

class BookSubject(_message.Message):
    __slots__ = ("name", "query", "subjectId")
    NAME_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    SUBJECTID_FIELD_NUMBER: _ClassVar[int]
    name: str
    query: str
    subjectId: str
    def __init__(self, name: _Optional[str] = ..., query: _Optional[str] = ..., subjectId: _Optional[str] = ...) -> None: ...

class BrowseLink(_message.Message):
    __slots__ = ("name", "dataUrl", "icon", "unknownCategoryContainer")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DATAURL_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    UNKNOWNCATEGORYCONTAINER_FIELD_NUMBER: _ClassVar[int]
    name: str
    dataUrl: str
    icon: Image
    unknownCategoryContainer: UnknownCategoryContainer
    def __init__(self, name: _Optional[str] = ..., dataUrl: _Optional[str] = ..., icon: _Optional[_Union[Image, _Mapping]] = ..., unknownCategoryContainer: _Optional[_Union[UnknownCategoryContainer, _Mapping]] = ...) -> None: ...

class UnknownCategoryContainer(_message.Message):
    __slots__ = ("categoryIdContainer",)
    CATEGORYIDCONTAINER_FIELD_NUMBER: _ClassVar[int]
    categoryIdContainer: CategoryIdContainer
    def __init__(self, categoryIdContainer: _Optional[_Union[CategoryIdContainer, _Mapping]] = ...) -> None: ...

class CategoryIdContainer(_message.Message):
    __slots__ = ("categoryId",)
    CATEGORYID_FIELD_NUMBER: _ClassVar[int]
    categoryId: str
    def __init__(self, categoryId: _Optional[str] = ...) -> None: ...

class BrowseResponse(_message.Message):
    __slots__ = ("contentsUrl", "promoUrl", "category", "breadcrumb", "categoryContainer")
    CONTENTSURL_FIELD_NUMBER: _ClassVar[int]
    PROMOURL_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    BREADCRUMB_FIELD_NUMBER: _ClassVar[int]
    CATEGORYCONTAINER_FIELD_NUMBER: _ClassVar[int]
    contentsUrl: str
    promoUrl: str
    category: _containers.RepeatedCompositeFieldContainer[BrowseLink]
    breadcrumb: _containers.RepeatedCompositeFieldContainer[BrowseLink]
    categoryContainer: CategoryContainer
    def __init__(self, contentsUrl: _Optional[str] = ..., promoUrl: _Optional[str] = ..., category: _Optional[_Iterable[_Union[BrowseLink, _Mapping]]] = ..., breadcrumb: _Optional[_Iterable[_Union[BrowseLink, _Mapping]]] = ..., categoryContainer: _Optional[_Union[CategoryContainer, _Mapping]] = ...) -> None: ...

class CategoryContainer(_message.Message):
    __slots__ = ("category",)
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    category: _containers.RepeatedCompositeFieldContainer[BrowseLink]
    def __init__(self, category: _Optional[_Iterable[_Union[BrowseLink, _Mapping]]] = ...) -> None: ...

class AddressChallenge(_message.Message):
    __slots__ = ("responseAddressParam", "responseCheckboxesParam", "title", "descriptionHtml", "checkbox", "address", "errorInputField", "errorHtml", "requiredField")
    RESPONSEADDRESSPARAM_FIELD_NUMBER: _ClassVar[int]
    RESPONSECHECKBOXESPARAM_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTIONHTML_FIELD_NUMBER: _ClassVar[int]
    CHECKBOX_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ERRORINPUTFIELD_FIELD_NUMBER: _ClassVar[int]
    ERRORHTML_FIELD_NUMBER: _ClassVar[int]
    REQUIREDFIELD_FIELD_NUMBER: _ClassVar[int]
    responseAddressParam: str
    responseCheckboxesParam: str
    title: str
    descriptionHtml: str
    checkbox: _containers.RepeatedCompositeFieldContainer[FormCheckbox]
    address: Address
    errorInputField: _containers.RepeatedCompositeFieldContainer[InputValidationError]
    errorHtml: str
    requiredField: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, responseAddressParam: _Optional[str] = ..., responseCheckboxesParam: _Optional[str] = ..., title: _Optional[str] = ..., descriptionHtml: _Optional[str] = ..., checkbox: _Optional[_Iterable[_Union[FormCheckbox, _Mapping]]] = ..., address: _Optional[_Union[Address, _Mapping]] = ..., errorInputField: _Optional[_Iterable[_Union[InputValidationError, _Mapping]]] = ..., errorHtml: _Optional[str] = ..., requiredField: _Optional[_Iterable[int]] = ...) -> None: ...

class AuthenticationChallenge(_message.Message):
    __slots__ = ("authenticationType", "responseAuthenticationTypeParam", "responseRetryCountParam", "pinHeaderText", "pinDescriptionTextHtml", "gaiaHeaderText", "gaiaDescriptionTextHtml")
    AUTHENTICATIONTYPE_FIELD_NUMBER: _ClassVar[int]
    RESPONSEAUTHENTICATIONTYPEPARAM_FIELD_NUMBER: _ClassVar[int]
    RESPONSERETRYCOUNTPARAM_FIELD_NUMBER: _ClassVar[int]
    PINHEADERTEXT_FIELD_NUMBER: _ClassVar[int]
    PINDESCRIPTIONTEXTHTML_FIELD_NUMBER: _ClassVar[int]
    GAIAHEADERTEXT_FIELD_NUMBER: _ClassVar[int]
    GAIADESCRIPTIONTEXTHTML_FIELD_NUMBER: _ClassVar[int]
    authenticationType: int
    responseAuthenticationTypeParam: str
    responseRetryCountParam: str
    pinHeaderText: str
    pinDescriptionTextHtml: str
    gaiaHeaderText: str
    gaiaDescriptionTextHtml: str
    def __init__(self, authenticationType: _Optional[int] = ..., responseAuthenticationTypeParam: _Optional[str] = ..., responseRetryCountParam: _Optional[str] = ..., pinHeaderText: _Optional[str] = ..., pinDescriptionTextHtml: _Optional[str] = ..., gaiaHeaderText: _Optional[str] = ..., gaiaDescriptionTextHtml: _Optional[str] = ...) -> None: ...

class BuyResponse(_message.Message):
    __slots__ = ("purchaseResponse", "checkoutinfo", "continueViaUrl", "purchaseStatusUrl", "checkoutServiceId", "checkoutTokenRequired", "baseCheckoutUrl", "tosCheckboxHtml", "iabPermissionError", "purchaseStatusResponse", "purchaseCookie", "challenge", "downloadToken")
    class CheckoutInfo(_message.Message):
        __slots__ = ("item", "subItem", "checkoutoption", "deprecatedCheckoutUrl", "addInstrumentUrl", "footerHtml", "eligibleInstrumentFamily", "footnoteHtml", "eligibleInstrument")
        class CheckoutOption(_message.Message):
            __slots__ = ("formOfPayment", "encodedAdjustedCart", "instrumentId", "item", "subItem", "total", "footerHtml", "instrumentFamily", "deprecatedInstrumentInapplicableReason", "selectedInstrument", "summary", "footnoteHtml", "instrument", "purchaseCookie", "disabledReason")
            FORMOFPAYMENT_FIELD_NUMBER: _ClassVar[int]
            ENCODEDADJUSTEDCART_FIELD_NUMBER: _ClassVar[int]
            INSTRUMENTID_FIELD_NUMBER: _ClassVar[int]
            ITEM_FIELD_NUMBER: _ClassVar[int]
            SUBITEM_FIELD_NUMBER: _ClassVar[int]
            TOTAL_FIELD_NUMBER: _ClassVar[int]
            FOOTERHTML_FIELD_NUMBER: _ClassVar[int]
            INSTRUMENTFAMILY_FIELD_NUMBER: _ClassVar[int]
            DEPRECATEDINSTRUMENTINAPPLICABLEREASON_FIELD_NUMBER: _ClassVar[int]
            SELECTEDINSTRUMENT_FIELD_NUMBER: _ClassVar[int]
            SUMMARY_FIELD_NUMBER: _ClassVar[int]
            FOOTNOTEHTML_FIELD_NUMBER: _ClassVar[int]
            INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
            PURCHASECOOKIE_FIELD_NUMBER: _ClassVar[int]
            DISABLEDREASON_FIELD_NUMBER: _ClassVar[int]
            formOfPayment: str
            encodedAdjustedCart: str
            instrumentId: str
            item: _containers.RepeatedCompositeFieldContainer[LineItem]
            subItem: _containers.RepeatedCompositeFieldContainer[LineItem]
            total: LineItem
            footerHtml: _containers.RepeatedScalarFieldContainer[str]
            instrumentFamily: int
            deprecatedInstrumentInapplicableReason: _containers.RepeatedScalarFieldContainer[int]
            selectedInstrument: bool
            summary: LineItem
            footnoteHtml: _containers.RepeatedScalarFieldContainer[str]
            instrument: Instrument
            purchaseCookie: str
            disabledReason: _containers.RepeatedScalarFieldContainer[str]
            def __init__(self, formOfPayment: _Optional[str] = ..., encodedAdjustedCart: _Optional[str] = ..., instrumentId: _Optional[str] = ..., item: _Optional[_Iterable[_Union[LineItem, _Mapping]]] = ..., subItem: _Optional[_Iterable[_Union[LineItem, _Mapping]]] = ..., total: _Optional[_Union[LineItem, _Mapping]] = ..., footerHtml: _Optional[_Iterable[str]] = ..., instrumentFamily: _Optional[int] = ..., deprecatedInstrumentInapplicableReason: _Optional[_Iterable[int]] = ..., selectedInstrument: _Optional[bool] = ..., summary: _Optional[_Union[LineItem, _Mapping]] = ..., footnoteHtml: _Optional[_Iterable[str]] = ..., instrument: _Optional[_Union[Instrument, _Mapping]] = ..., purchaseCookie: _Optional[str] = ..., disabledReason: _Optional[_Iterable[str]] = ...) -> None: ...
        ITEM_FIELD_NUMBER: _ClassVar[int]
        SUBITEM_FIELD_NUMBER: _ClassVar[int]
        CHECKOUTOPTION_FIELD_NUMBER: _ClassVar[int]
        DEPRECATEDCHECKOUTURL_FIELD_NUMBER: _ClassVar[int]
        ADDINSTRUMENTURL_FIELD_NUMBER: _ClassVar[int]
        FOOTERHTML_FIELD_NUMBER: _ClassVar[int]
        ELIGIBLEINSTRUMENTFAMILY_FIELD_NUMBER: _ClassVar[int]
        FOOTNOTEHTML_FIELD_NUMBER: _ClassVar[int]
        ELIGIBLEINSTRUMENT_FIELD_NUMBER: _ClassVar[int]
        item: LineItem
        subItem: _containers.RepeatedCompositeFieldContainer[LineItem]
        checkoutoption: _containers.RepeatedCompositeFieldContainer[BuyResponse.CheckoutInfo.CheckoutOption]
        deprecatedCheckoutUrl: str
        addInstrumentUrl: str
        footerHtml: _containers.RepeatedScalarFieldContainer[str]
        eligibleInstrumentFamily: _containers.RepeatedScalarFieldContainer[int]
        footnoteHtml: _containers.RepeatedScalarFieldContainer[str]
        eligibleInstrument: _containers.RepeatedCompositeFieldContainer[Instrument]
        def __init__(self, item: _Optional[_Union[LineItem, _Mapping]] = ..., subItem: _Optional[_Iterable[_Union[LineItem, _Mapping]]] = ..., checkoutoption: _Optional[_Iterable[_Union[BuyResponse.CheckoutInfo.CheckoutOption, _Mapping]]] = ..., deprecatedCheckoutUrl: _Optional[str] = ..., addInstrumentUrl: _Optional[str] = ..., footerHtml: _Optional[_Iterable[str]] = ..., eligibleInstrumentFamily: _Optional[_Iterable[int]] = ..., footnoteHtml: _Optional[_Iterable[str]] = ..., eligibleInstrument: _Optional[_Iterable[_Union[Instrument, _Mapping]]] = ...) -> None: ...
    PURCHASERESPONSE_FIELD_NUMBER: _ClassVar[int]
    CHECKOUTINFO_FIELD_NUMBER: _ClassVar[int]
    CONTINUEVIAURL_FIELD_NUMBER: _ClassVar[int]
    PURCHASESTATUSURL_FIELD_NUMBER: _ClassVar[int]
    CHECKOUTSERVICEID_FIELD_NUMBER: _ClassVar[int]
    CHECKOUTTOKENREQUIRED_FIELD_NUMBER: _ClassVar[int]
    BASECHECKOUTURL_FIELD_NUMBER: _ClassVar[int]
    TOSCHECKBOXHTML_FIELD_NUMBER: _ClassVar[int]
    IABPERMISSIONERROR_FIELD_NUMBER: _ClassVar[int]
    PURCHASESTATUSRESPONSE_FIELD_NUMBER: _ClassVar[int]
    PURCHASECOOKIE_FIELD_NUMBER: _ClassVar[int]
    CHALLENGE_FIELD_NUMBER: _ClassVar[int]
    DOWNLOADTOKEN_FIELD_NUMBER: _ClassVar[int]
    purchaseResponse: PurchaseNotificationResponse
    checkoutinfo: BuyResponse.CheckoutInfo
    continueViaUrl: str
    purchaseStatusUrl: str
    checkoutServiceId: str
    checkoutTokenRequired: bool
    baseCheckoutUrl: str
    tosCheckboxHtml: _containers.RepeatedScalarFieldContainer[str]
    iabPermissionError: int
    purchaseStatusResponse: PurchaseStatusResponse
    purchaseCookie: str
    challenge: Challenge
    downloadToken: str
    def __init__(self, purchaseResponse: _Optional[_Union[PurchaseNotificationResponse, _Mapping]] = ..., checkoutinfo: _Optional[_Union[BuyResponse.CheckoutInfo, _Mapping]] = ..., continueViaUrl: _Optional[str] = ..., purchaseStatusUrl: _Optional[str] = ..., checkoutServiceId: _Optional[str] = ..., checkoutTokenRequired: _Optional[bool] = ..., baseCheckoutUrl: _Optional[str] = ..., tosCheckboxHtml: _Optional[_Iterable[str]] = ..., iabPermissionError: _Optional[int] = ..., purchaseStatusResponse: _Optional[_Union[PurchaseStatusResponse, _Mapping]] = ..., purchaseCookie: _Optional[str] = ..., challenge: _Optional[_Union[Challenge, _Mapping]] = ..., downloadToken: _Optional[str] = ...) -> None: ...

class Challenge(_message.Message):
    __slots__ = ("addressChallenge", "authenticationChallenge")
    ADDRESSCHALLENGE_FIELD_NUMBER: _ClassVar[int]
    AUTHENTICATIONCHALLENGE_FIELD_NUMBER: _ClassVar[int]
    addressChallenge: AddressChallenge
    authenticationChallenge: AuthenticationChallenge
    def __init__(self, addressChallenge: _Optional[_Union[AddressChallenge, _Mapping]] = ..., authenticationChallenge: _Optional[_Union[AuthenticationChallenge, _Mapping]] = ...) -> None: ...

class FormCheckbox(_message.Message):
    __slots__ = ("description", "checked", "required")
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CHECKED_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FIELD_NUMBER: _ClassVar[int]
    description: str
    checked: bool
    required: bool
    def __init__(self, description: _Optional[str] = ..., checked: _Optional[bool] = ..., required: _Optional[bool] = ...) -> None: ...

class LineItem(_message.Message):
    __slots__ = ("name", "description", "offer", "amount")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    OFFER_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    offer: Offer
    amount: Money
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., offer: _Optional[_Union[Offer, _Mapping]] = ..., amount: _Optional[_Union[Money, _Mapping]] = ...) -> None: ...

class Money(_message.Message):
    __slots__ = ("micros", "currencyCode", "formattedAmount")
    MICROS_FIELD_NUMBER: _ClassVar[int]
    CURRENCYCODE_FIELD_NUMBER: _ClassVar[int]
    FORMATTEDAMOUNT_FIELD_NUMBER: _ClassVar[int]
    micros: int
    currencyCode: str
    formattedAmount: str
    def __init__(self, micros: _Optional[int] = ..., currencyCode: _Optional[str] = ..., formattedAmount: _Optional[str] = ...) -> None: ...

class PurchaseNotificationResponse(_message.Message):
    __slots__ = ("status", "debugInfo", "localizedErrorMessage", "purchaseId")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DEBUGINFO_FIELD_NUMBER: _ClassVar[int]
    LOCALIZEDERRORMESSAGE_FIELD_NUMBER: _ClassVar[int]
    PURCHASEID_FIELD_NUMBER: _ClassVar[int]
    status: int
    debugInfo: DebugInfo
    localizedErrorMessage: str
    purchaseId: str
    def __init__(self, status: _Optional[int] = ..., debugInfo: _Optional[_Union[DebugInfo, _Mapping]] = ..., localizedErrorMessage: _Optional[str] = ..., purchaseId: _Optional[str] = ...) -> None: ...

class PurchaseStatusResponse(_message.Message):
    __slots__ = ("status", "statusMsg", "statusTitle", "briefMessage", "infoUrl", "libraryUpdate", "rejectedInstrument", "appDeliveryData")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STATUSMSG_FIELD_NUMBER: _ClassVar[int]
    STATUSTITLE_FIELD_NUMBER: _ClassVar[int]
    BRIEFMESSAGE_FIELD_NUMBER: _ClassVar[int]
    INFOURL_FIELD_NUMBER: _ClassVar[int]
    LIBRARYUPDATE_FIELD_NUMBER: _ClassVar[int]
    REJECTEDINSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    APPDELIVERYDATA_FIELD_NUMBER: _ClassVar[int]
    status: int
    statusMsg: str
    statusTitle: str
    briefMessage: str
    infoUrl: str
    libraryUpdate: LibraryUpdate
    rejectedInstrument: Instrument
    appDeliveryData: AndroidAppDeliveryData
    def __init__(self, status: _Optional[int] = ..., statusMsg: _Optional[str] = ..., statusTitle: _Optional[str] = ..., briefMessage: _Optional[str] = ..., infoUrl: _Optional[str] = ..., libraryUpdate: _Optional[_Union[LibraryUpdate, _Mapping]] = ..., rejectedInstrument: _Optional[_Union[Instrument, _Mapping]] = ..., appDeliveryData: _Optional[_Union[AndroidAppDeliveryData, _Mapping]] = ...) -> None: ...

class DeliveryResponse(_message.Message):
    __slots__ = ("appDeliveryData",)
    APPDELIVERYDATA_FIELD_NUMBER: _ClassVar[int]
    appDeliveryData: AndroidAppDeliveryData
    def __init__(self, appDeliveryData: _Optional[_Union[AndroidAppDeliveryData, _Mapping]] = ...) -> None: ...

class Docid(_message.Message):
    __slots__ = ("backendDocid", "type", "backend")
    BACKENDDOCID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    BACKEND_FIELD_NUMBER: _ClassVar[int]
    backendDocid: str
    type: int
    backend: int
    def __init__(self, backendDocid: _Optional[str] = ..., type: _Optional[int] = ..., backend: _Optional[int] = ...) -> None: ...

class Install(_message.Message):
    __slots__ = ("androidId", "version", "bundled")
    ANDROIDID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    BUNDLED_FIELD_NUMBER: _ClassVar[int]
    androidId: int
    version: int
    bundled: bool
    def __init__(self, androidId: _Optional[int] = ..., version: _Optional[int] = ..., bundled: _Optional[bool] = ...) -> None: ...

class Offer(_message.Message):
    __slots__ = ("micros", "currencyCode", "formattedAmount", "convertedPrice", "checkoutFlowRequired", "fullPriceMicros", "formattedFullAmount", "offerType", "rentalTerms", "onSaleDate", "promotionLabel", "subscriptionTerms", "formattedName", "formattedDescription", "sale", "message", "saleEndTimestamp", "saleMessage")
    MICROS_FIELD_NUMBER: _ClassVar[int]
    CURRENCYCODE_FIELD_NUMBER: _ClassVar[int]
    FORMATTEDAMOUNT_FIELD_NUMBER: _ClassVar[int]
    CONVERTEDPRICE_FIELD_NUMBER: _ClassVar[int]
    CHECKOUTFLOWREQUIRED_FIELD_NUMBER: _ClassVar[int]
    FULLPRICEMICROS_FIELD_NUMBER: _ClassVar[int]
    FORMATTEDFULLAMOUNT_FIELD_NUMBER: _ClassVar[int]
    OFFERTYPE_FIELD_NUMBER: _ClassVar[int]
    RENTALTERMS_FIELD_NUMBER: _ClassVar[int]
    ONSALEDATE_FIELD_NUMBER: _ClassVar[int]
    PROMOTIONLABEL_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTIONTERMS_FIELD_NUMBER: _ClassVar[int]
    FORMATTEDNAME_FIELD_NUMBER: _ClassVar[int]
    FORMATTEDDESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SALE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SALEENDTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    SALEMESSAGE_FIELD_NUMBER: _ClassVar[int]
    micros: int
    currencyCode: str
    formattedAmount: str
    convertedPrice: _containers.RepeatedCompositeFieldContainer[Offer]
    checkoutFlowRequired: bool
    fullPriceMicros: int
    formattedFullAmount: str
    offerType: int
    rentalTerms: RentalTerms
    onSaleDate: int
    promotionLabel: _containers.RepeatedScalarFieldContainer[str]
    subscriptionTerms: SubscriptionTerms
    formattedName: str
    formattedDescription: str
    sale: bool
    message: str
    saleEndTimestamp: int
    saleMessage: str
    def __init__(self, micros: _Optional[int] = ..., currencyCode: _Optional[str] = ..., formattedAmount: _Optional[str] = ..., convertedPrice: _Optional[_Iterable[_Union[Offer, _Mapping]]] = ..., checkoutFlowRequired: _Optional[bool] = ..., fullPriceMicros: _Optional[int] = ..., formattedFullAmount: _Optional[str] = ..., offerType: _Optional[int] = ..., rentalTerms: _Optional[_Union[RentalTerms, _Mapping]] = ..., onSaleDate: _Optional[int] = ..., promotionLabel: _Optional[_Iterable[str]] = ..., subscriptionTerms: _Optional[_Union[SubscriptionTerms, _Mapping]] = ..., formattedName: _Optional[str] = ..., formattedDescription: _Optional[str] = ..., sale: _Optional[bool] = ..., message: _Optional[str] = ..., saleEndTimestamp: _Optional[int] = ..., saleMessage: _Optional[str] = ...) -> None: ...

class OwnershipInfo(_message.Message):
    __slots__ = ("initiationTimestampMsec", "validUntilTimestampMsec", "autoRenewing", "refundTimeoutTimestampMsec", "postDeliveryRefundWindowMsec")
    INITIATIONTIMESTAMPMSEC_FIELD_NUMBER: _ClassVar[int]
    VALIDUNTILTIMESTAMPMSEC_FIELD_NUMBER: _ClassVar[int]
    AUTORENEWING_FIELD_NUMBER: _ClassVar[int]
    REFUNDTIMEOUTTIMESTAMPMSEC_FIELD_NUMBER: _ClassVar[int]
    POSTDELIVERYREFUNDWINDOWMSEC_FIELD_NUMBER: _ClassVar[int]
    initiationTimestampMsec: int
    validUntilTimestampMsec: int
    autoRenewing: bool
    refundTimeoutTimestampMsec: int
    postDeliveryRefundWindowMsec: int
    def __init__(self, initiationTimestampMsec: _Optional[int] = ..., validUntilTimestampMsec: _Optional[int] = ..., autoRenewing: _Optional[bool] = ..., refundTimeoutTimestampMsec: _Optional[int] = ..., postDeliveryRefundWindowMsec: _Optional[int] = ...) -> None: ...

class RentalTerms(_message.Message):
    __slots__ = ("grantPeriodSeconds", "activatePeriodSeconds")
    GRANTPERIODSECONDS_FIELD_NUMBER: _ClassVar[int]
    ACTIVATEPERIODSECONDS_FIELD_NUMBER: _ClassVar[int]
    grantPeriodSeconds: int
    activatePeriodSeconds: int
    def __init__(self, grantPeriodSeconds: _Optional[int] = ..., activatePeriodSeconds: _Optional[int] = ...) -> None: ...

class SubscriptionTerms(_message.Message):
    __slots__ = ("recurringPeriod", "trialPeriod")
    RECURRINGPERIOD_FIELD_NUMBER: _ClassVar[int]
    TRIALPERIOD_FIELD_NUMBER: _ClassVar[int]
    recurringPeriod: TimePeriod
    trialPeriod: TimePeriod
    def __init__(self, recurringPeriod: _Optional[_Union[TimePeriod, _Mapping]] = ..., trialPeriod: _Optional[_Union[TimePeriod, _Mapping]] = ...) -> None: ...

class TimePeriod(_message.Message):
    __slots__ = ("unit", "count")
    UNIT_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    unit: int
    count: int
    def __init__(self, unit: _Optional[int] = ..., count: _Optional[int] = ...) -> None: ...

class BillingAddressSpec(_message.Message):
    __slots__ = ("billingAddressType", "requiredField")
    BILLINGADDRESSTYPE_FIELD_NUMBER: _ClassVar[int]
    REQUIREDFIELD_FIELD_NUMBER: _ClassVar[int]
    billingAddressType: int
    requiredField: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, billingAddressType: _Optional[int] = ..., requiredField: _Optional[_Iterable[int]] = ...) -> None: ...

class CarrierBillingCredentials(_message.Message):
    __slots__ = ("value", "expiration")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_FIELD_NUMBER: _ClassVar[int]
    value: str
    expiration: int
    def __init__(self, value: _Optional[str] = ..., expiration: _Optional[int] = ...) -> None: ...

class CarrierBillingInstrument(_message.Message):
    __slots__ = ("instrumentKey", "accountType", "currencyCode", "transactionLimit", "subscriberIdentifier", "encryptedSubscriberInfo", "credentials", "acceptedCarrierTos")
    INSTRUMENTKEY_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTTYPE_FIELD_NUMBER: _ClassVar[int]
    CURRENCYCODE_FIELD_NUMBER: _ClassVar[int]
    TRANSACTIONLIMIT_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIBERIDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTEDSUBSCRIBERINFO_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    ACCEPTEDCARRIERTOS_FIELD_NUMBER: _ClassVar[int]
    instrumentKey: str
    accountType: str
    currencyCode: str
    transactionLimit: int
    subscriberIdentifier: str
    encryptedSubscriberInfo: EncryptedSubscriberInfo
    credentials: CarrierBillingCredentials
    acceptedCarrierTos: CarrierTos
    def __init__(self, instrumentKey: _Optional[str] = ..., accountType: _Optional[str] = ..., currencyCode: _Optional[str] = ..., transactionLimit: _Optional[int] = ..., subscriberIdentifier: _Optional[str] = ..., encryptedSubscriberInfo: _Optional[_Union[EncryptedSubscriberInfo, _Mapping]] = ..., credentials: _Optional[_Union[CarrierBillingCredentials, _Mapping]] = ..., acceptedCarrierTos: _Optional[_Union[CarrierTos, _Mapping]] = ...) -> None: ...

class CarrierBillingInstrumentStatus(_message.Message):
    __slots__ = ("carrierTos", "associationRequired", "passwordRequired", "carrierPasswordPrompt", "apiVersion", "name")
    CARRIERTOS_FIELD_NUMBER: _ClassVar[int]
    ASSOCIATIONREQUIRED_FIELD_NUMBER: _ClassVar[int]
    PASSWORDREQUIRED_FIELD_NUMBER: _ClassVar[int]
    CARRIERPASSWORDPROMPT_FIELD_NUMBER: _ClassVar[int]
    APIVERSION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    carrierTos: CarrierTos
    associationRequired: bool
    passwordRequired: bool
    carrierPasswordPrompt: PasswordPrompt
    apiVersion: int
    name: str
    def __init__(self, carrierTos: _Optional[_Union[CarrierTos, _Mapping]] = ..., associationRequired: _Optional[bool] = ..., passwordRequired: _Optional[bool] = ..., carrierPasswordPrompt: _Optional[_Union[PasswordPrompt, _Mapping]] = ..., apiVersion: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...

class CarrierTos(_message.Message):
    __slots__ = ("dcbTos", "piiTos", "needsDcbTosAcceptance", "needsPiiTosAcceptance")
    DCBTOS_FIELD_NUMBER: _ClassVar[int]
    PIITOS_FIELD_NUMBER: _ClassVar[int]
    NEEDSDCBTOSACCEPTANCE_FIELD_NUMBER: _ClassVar[int]
    NEEDSPIITOSACCEPTANCE_FIELD_NUMBER: _ClassVar[int]
    dcbTos: CarrierTosEntry
    piiTos: CarrierTosEntry
    needsDcbTosAcceptance: bool
    needsPiiTosAcceptance: bool
    def __init__(self, dcbTos: _Optional[_Union[CarrierTosEntry, _Mapping]] = ..., piiTos: _Optional[_Union[CarrierTosEntry, _Mapping]] = ..., needsDcbTosAcceptance: _Optional[bool] = ..., needsPiiTosAcceptance: _Optional[bool] = ...) -> None: ...

class CarrierTosEntry(_message.Message):
    __slots__ = ("url", "version")
    URL_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    url: str
    version: str
    def __init__(self, url: _Optional[str] = ..., version: _Optional[str] = ...) -> None: ...

class CreditCardInstrument(_message.Message):
    __slots__ = ("type", "escrowHandle", "lastDigits", "expirationMonth", "expirationYear", "escrowEfeParam")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ESCROWHANDLE_FIELD_NUMBER: _ClassVar[int]
    LASTDIGITS_FIELD_NUMBER: _ClassVar[int]
    EXPIRATIONMONTH_FIELD_NUMBER: _ClassVar[int]
    EXPIRATIONYEAR_FIELD_NUMBER: _ClassVar[int]
    ESCROWEFEPARAM_FIELD_NUMBER: _ClassVar[int]
    type: int
    escrowHandle: str
    lastDigits: str
    expirationMonth: int
    expirationYear: int
    escrowEfeParam: _containers.RepeatedCompositeFieldContainer[EfeParam]
    def __init__(self, type: _Optional[int] = ..., escrowHandle: _Optional[str] = ..., lastDigits: _Optional[str] = ..., expirationMonth: _Optional[int] = ..., expirationYear: _Optional[int] = ..., escrowEfeParam: _Optional[_Iterable[_Union[EfeParam, _Mapping]]] = ...) -> None: ...

class EfeParam(_message.Message):
    __slots__ = ("key", "value")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: int
    value: str
    def __init__(self, key: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...

class InputValidationError(_message.Message):
    __slots__ = ("inputField", "errorMessage")
    INPUTFIELD_FIELD_NUMBER: _ClassVar[int]
    ERRORMESSAGE_FIELD_NUMBER: _ClassVar[int]
    inputField: int
    errorMessage: str
    def __init__(self, inputField: _Optional[int] = ..., errorMessage: _Optional[str] = ...) -> None: ...

class Instrument(_message.Message):
    __slots__ = ("instrumentId", "billingAddress", "creditCard", "carrierBilling", "billingAddressSpec", "instrumentFamily", "carrierBillingStatus", "displayTitle")
    INSTRUMENTID_FIELD_NUMBER: _ClassVar[int]
    BILLINGADDRESS_FIELD_NUMBER: _ClassVar[int]
    CREDITCARD_FIELD_NUMBER: _ClassVar[int]
    CARRIERBILLING_FIELD_NUMBER: _ClassVar[int]
    BILLINGADDRESSSPEC_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENTFAMILY_FIELD_NUMBER: _ClassVar[int]
    CARRIERBILLINGSTATUS_FIELD_NUMBER: _ClassVar[int]
    DISPLAYTITLE_FIELD_NUMBER: _ClassVar[int]
    instrumentId: str
    billingAddress: Address
    creditCard: CreditCardInstrument
    carrierBilling: CarrierBillingInstrument
    billingAddressSpec: BillingAddressSpec
    instrumentFamily: int
    carrierBillingStatus: CarrierBillingInstrumentStatus
    displayTitle: str
    def __init__(self, instrumentId: _Optional[str] = ..., billingAddress: _Optional[_Union[Address, _Mapping]] = ..., creditCard: _Optional[_Union[CreditCardInstrument, _Mapping]] = ..., carrierBilling: _Optional[_Union[CarrierBillingInstrument, _Mapping]] = ..., billingAddressSpec: _Optional[_Union[BillingAddressSpec, _Mapping]] = ..., instrumentFamily: _Optional[int] = ..., carrierBillingStatus: _Optional[_Union[CarrierBillingInstrumentStatus, _Mapping]] = ..., displayTitle: _Optional[str] = ...) -> None: ...

class PasswordPrompt(_message.Message):
    __slots__ = ("prompt", "forgotPasswordUrl")
    PROMPT_FIELD_NUMBER: _ClassVar[int]
    FORGOTPASSWORDURL_FIELD_NUMBER: _ClassVar[int]
    prompt: str
    forgotPasswordUrl: str
    def __init__(self, prompt: _Optional[str] = ..., forgotPasswordUrl: _Optional[str] = ...) -> None: ...

class ContainerMetadata(_message.Message):
    __slots__ = ("browseUrl", "nextPageUrl", "relevance", "estimatedResults", "analyticsCookie", "ordered")
    BROWSEURL_FIELD_NUMBER: _ClassVar[int]
    NEXTPAGEURL_FIELD_NUMBER: _ClassVar[int]
    RELEVANCE_FIELD_NUMBER: _ClassVar[int]
    ESTIMATEDRESULTS_FIELD_NUMBER: _ClassVar[int]
    ANALYTICSCOOKIE_FIELD_NUMBER: _ClassVar[int]
    ORDERED_FIELD_NUMBER: _ClassVar[int]
    browseUrl: str
    nextPageUrl: str
    relevance: float
    estimatedResults: int
    analyticsCookie: str
    ordered: bool
    def __init__(self, browseUrl: _Optional[str] = ..., nextPageUrl: _Optional[str] = ..., relevance: _Optional[float] = ..., estimatedResults: _Optional[int] = ..., analyticsCookie: _Optional[str] = ..., ordered: _Optional[bool] = ...) -> None: ...

class DebugInfo(_message.Message):
    __slots__ = ("message", "timing")
    class Timing(_message.Message):
        __slots__ = ("name", "timeInMs")
        NAME_FIELD_NUMBER: _ClassVar[int]
        TIMEINMS_FIELD_NUMBER: _ClassVar[int]
        name: str
        timeInMs: float
        def __init__(self, name: _Optional[str] = ..., timeInMs: _Optional[float] = ...) -> None: ...
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TIMING_FIELD_NUMBER: _ClassVar[int]
    message: _containers.RepeatedScalarFieldContainer[str]
    timing: _containers.RepeatedCompositeFieldContainer[DebugInfo.Timing]
    def __init__(self, message: _Optional[_Iterable[str]] = ..., timing: _Optional[_Iterable[_Union[DebugInfo.Timing, _Mapping]]] = ...) -> None: ...

class BulkDetailsEntry(_message.Message):
    __slots__ = ("doc",)
    DOC_FIELD_NUMBER: _ClassVar[int]
    doc: DocV2
    def __init__(self, doc: _Optional[_Union[DocV2, _Mapping]] = ...) -> None: ...

class BulkDetailsRequest(_message.Message):
    __slots__ = ("docid", "includeChildDocs")
    DOCID_FIELD_NUMBER: _ClassVar[int]
    INCLUDECHILDDOCS_FIELD_NUMBER: _ClassVar[int]
    docid: _containers.RepeatedScalarFieldContainer[str]
    includeChildDocs: bool
    def __init__(self, docid: _Optional[_Iterable[str]] = ..., includeChildDocs: _Optional[bool] = ...) -> None: ...

class BulkDetailsResponse(_message.Message):
    __slots__ = ("entry",)
    ENTRY_FIELD_NUMBER: _ClassVar[int]
    entry: _containers.RepeatedCompositeFieldContainer[BulkDetailsEntry]
    def __init__(self, entry: _Optional[_Iterable[_Union[BulkDetailsEntry, _Mapping]]] = ...) -> None: ...

class DetailsResponse(_message.Message):
    __slots__ = ("docV1", "analyticsCookie", "userReview", "docV2", "footerHtml", "badge", "features", "detailsStreamUrl", "userReviewUrl", "postAcquireDetailsStreamUrl")
    DOCV1_FIELD_NUMBER: _ClassVar[int]
    ANALYTICSCOOKIE_FIELD_NUMBER: _ClassVar[int]
    USERREVIEW_FIELD_NUMBER: _ClassVar[int]
    DOCV2_FIELD_NUMBER: _ClassVar[int]
    FOOTERHTML_FIELD_NUMBER: _ClassVar[int]
    BADGE_FIELD_NUMBER: _ClassVar[int]
    FEATURES_FIELD_NUMBER: _ClassVar[int]
    DETAILSSTREAMURL_FIELD_NUMBER: _ClassVar[int]
    USERREVIEWURL_FIELD_NUMBER: _ClassVar[int]
    POSTACQUIREDETAILSSTREAMURL_FIELD_NUMBER: _ClassVar[int]
    docV1: DocV1
    analyticsCookie: str
    userReview: Review
    docV2: DocV2
    footerHtml: str
    badge: _containers.RepeatedCompositeFieldContainer[Badge]
    features: Features
    detailsStreamUrl: str
    userReviewUrl: str
    postAcquireDetailsStreamUrl: str
    def __init__(self, docV1: _Optional[_Union[DocV1, _Mapping]] = ..., analyticsCookie: _Optional[str] = ..., userReview: _Optional[_Union[Review, _Mapping]] = ..., docV2: _Optional[_Union[DocV2, _Mapping]] = ..., footerHtml: _Optional[str] = ..., badge: _Optional[_Iterable[_Union[Badge, _Mapping]]] = ..., features: _Optional[_Union[Features, _Mapping]] = ..., detailsStreamUrl: _Optional[str] = ..., userReviewUrl: _Optional[str] = ..., postAcquireDetailsStreamUrl: _Optional[str] = ...) -> None: ...

class Badge(_message.Message):
    __slots__ = ("label", "image", "badgeContainer1", "message")
    LABEL_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    BADGECONTAINER1_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    label: str
    image: Image
    badgeContainer1: BadgeContainer1
    message: str
    def __init__(self, label: _Optional[str] = ..., image: _Optional[_Union[Image, _Mapping]] = ..., badgeContainer1: _Optional[_Union[BadgeContainer1, _Mapping]] = ..., message: _Optional[str] = ...) -> None: ...

class BadgeContainer1(_message.Message):
    __slots__ = ("badgeContainer2",)
    BADGECONTAINER2_FIELD_NUMBER: _ClassVar[int]
    badgeContainer2: BadgeContainer2
    def __init__(self, badgeContainer2: _Optional[_Union[BadgeContainer2, _Mapping]] = ...) -> None: ...

class BadgeContainer2(_message.Message):
    __slots__ = ("badgeLinkContainer",)
    BADGELINKCONTAINER_FIELD_NUMBER: _ClassVar[int]
    badgeLinkContainer: BadgeLinkContainer
    def __init__(self, badgeLinkContainer: _Optional[_Union[BadgeLinkContainer, _Mapping]] = ...) -> None: ...

class BadgeLinkContainer(_message.Message):
    __slots__ = ("link",)
    LINK_FIELD_NUMBER: _ClassVar[int]
    link: str
    def __init__(self, link: _Optional[str] = ...) -> None: ...

class Features(_message.Message):
    __slots__ = ("featurePresence", "featureRating")
    FEATUREPRESENCE_FIELD_NUMBER: _ClassVar[int]
    FEATURERATING_FIELD_NUMBER: _ClassVar[int]
    featurePresence: _containers.RepeatedCompositeFieldContainer[Feature]
    featureRating: _containers.RepeatedCompositeFieldContainer[Feature]
    def __init__(self, featurePresence: _Optional[_Iterable[_Union[Feature, _Mapping]]] = ..., featureRating: _Optional[_Iterable[_Union[Feature, _Mapping]]] = ...) -> None: ...

class Feature(_message.Message):
    __slots__ = ("label", "value")
    LABEL_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    label: str
    value: str
    def __init__(self, label: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class DeviceConfigurationProto(_message.Message):
    __slots__ = ("touchScreen", "keyboard", "navigation", "screenLayout", "hasHardKeyboard", "hasFiveWayNavigation", "screenDensity", "glEsVersion", "systemSharedLibrary", "systemAvailableFeature", "nativePlatform", "screenWidth", "screenHeight", "systemSupportedLocale", "glExtension", "deviceClass", "maxApkDownloadSizeMb")
    TOUCHSCREEN_FIELD_NUMBER: _ClassVar[int]
    KEYBOARD_FIELD_NUMBER: _ClassVar[int]
    NAVIGATION_FIELD_NUMBER: _ClassVar[int]
    SCREENLAYOUT_FIELD_NUMBER: _ClassVar[int]
    HASHARDKEYBOARD_FIELD_NUMBER: _ClassVar[int]
    HASFIVEWAYNAVIGATION_FIELD_NUMBER: _ClassVar[int]
    SCREENDENSITY_FIELD_NUMBER: _ClassVar[int]
    GLESVERSION_FIELD_NUMBER: _ClassVar[int]
    SYSTEMSHAREDLIBRARY_FIELD_NUMBER: _ClassVar[int]
    SYSTEMAVAILABLEFEATURE_FIELD_NUMBER: _ClassVar[int]
    NATIVEPLATFORM_FIELD_NUMBER: _ClassVar[int]
    SCREENWIDTH_FIELD_NUMBER: _ClassVar[int]
    SCREENHEIGHT_FIELD_NUMBER: _ClassVar[int]
    SYSTEMSUPPORTEDLOCALE_FIELD_NUMBER: _ClassVar[int]
    GLEXTENSION_FIELD_NUMBER: _ClassVar[int]
    DEVICECLASS_FIELD_NUMBER: _ClassVar[int]
    MAXAPKDOWNLOADSIZEMB_FIELD_NUMBER: _ClassVar[int]
    touchScreen: int
    keyboard: int
    navigation: int
    screenLayout: int
    hasHardKeyboard: bool
    hasFiveWayNavigation: bool
    screenDensity: int
    glEsVersion: int
    systemSharedLibrary: _containers.RepeatedScalarFieldContainer[str]
    systemAvailableFeature: _containers.RepeatedScalarFieldContainer[str]
    nativePlatform: _containers.RepeatedScalarFieldContainer[str]
    screenWidth: int
    screenHeight: int
    systemSupportedLocale: _containers.RepeatedScalarFieldContainer[str]
    glExtension: _containers.RepeatedScalarFieldContainer[str]
    deviceClass: int
    maxApkDownloadSizeMb: int
    def __init__(self, touchScreen: _Optional[int] = ..., keyboard: _Optional[int] = ..., navigation: _Optional[int] = ..., screenLayout: _Optional[int] = ..., hasHardKeyboard: _Optional[bool] = ..., hasFiveWayNavigation: _Optional[bool] = ..., screenDensity: _Optional[int] = ..., glEsVersion: _Optional[int] = ..., systemSharedLibrary: _Optional[_Iterable[str]] = ..., systemAvailableFeature: _Optional[_Iterable[str]] = ..., nativePlatform: _Optional[_Iterable[str]] = ..., screenWidth: _Optional[int] = ..., screenHeight: _Optional[int] = ..., systemSupportedLocale: _Optional[_Iterable[str]] = ..., glExtension: _Optional[_Iterable[str]] = ..., deviceClass: _Optional[int] = ..., maxApkDownloadSizeMb: _Optional[int] = ...) -> None: ...

class Document(_message.Message):
    __slots__ = ("docid", "fetchDocid", "sampleDocid", "title", "url", "snippet", "priceDeprecated", "availability", "image", "child", "aggregateRating", "offer", "translatedSnippet", "documentVariant", "categoryId", "decoration", "parent", "privacyPolicyUrl")
    DOCID_FIELD_NUMBER: _ClassVar[int]
    FETCHDOCID_FIELD_NUMBER: _ClassVar[int]
    SAMPLEDOCID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    SNIPPET_FIELD_NUMBER: _ClassVar[int]
    PRICEDEPRECATED_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    CHILD_FIELD_NUMBER: _ClassVar[int]
    AGGREGATERATING_FIELD_NUMBER: _ClassVar[int]
    OFFER_FIELD_NUMBER: _ClassVar[int]
    TRANSLATEDSNIPPET_FIELD_NUMBER: _ClassVar[int]
    DOCUMENTVARIANT_FIELD_NUMBER: _ClassVar[int]
    CATEGORYID_FIELD_NUMBER: _ClassVar[int]
    DECORATION_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PRIVACYPOLICYURL_FIELD_NUMBER: _ClassVar[int]
    docid: Docid
    fetchDocid: Docid
    sampleDocid: Docid
    title: str
    url: str
    snippet: _containers.RepeatedScalarFieldContainer[str]
    priceDeprecated: Offer
    availability: Availability
    image: _containers.RepeatedCompositeFieldContainer[Image]
    child: _containers.RepeatedCompositeFieldContainer[Document]
    aggregateRating: AggregateRating
    offer: _containers.RepeatedCompositeFieldContainer[Offer]
    translatedSnippet: _containers.RepeatedCompositeFieldContainer[TranslatedText]
    documentVariant: _containers.RepeatedCompositeFieldContainer[DocumentVariant]
    categoryId: _containers.RepeatedScalarFieldContainer[str]
    decoration: _containers.RepeatedCompositeFieldContainer[Document]
    parent: _containers.RepeatedCompositeFieldContainer[Document]
    privacyPolicyUrl: str
    def __init__(self, docid: _Optional[_Union[Docid, _Mapping]] = ..., fetchDocid: _Optional[_Union[Docid, _Mapping]] = ..., sampleDocid: _Optional[_Union[Docid, _Mapping]] = ..., title: _Optional[str] = ..., url: _Optional[str] = ..., snippet: _Optional[_Iterable[str]] = ..., priceDeprecated: _Optional[_Union[Offer, _Mapping]] = ..., availability: _Optional[_Union[Availability, _Mapping]] = ..., image: _Optional[_Iterable[_Union[Image, _Mapping]]] = ..., child: _Optional[_Iterable[_Union[Document, _Mapping]]] = ..., aggregateRating: _Optional[_Union[AggregateRating, _Mapping]] = ..., offer: _Optional[_Iterable[_Union[Offer, _Mapping]]] = ..., translatedSnippet: _Optional[_Iterable[_Union[TranslatedText, _Mapping]]] = ..., documentVariant: _Optional[_Iterable[_Union[DocumentVariant, _Mapping]]] = ..., categoryId: _Optional[_Iterable[str]] = ..., decoration: _Optional[_Iterable[_Union[Document, _Mapping]]] = ..., parent: _Optional[_Iterable[_Union[Document, _Mapping]]] = ..., privacyPolicyUrl: _Optional[str] = ...) -> None: ...

class DocumentVariant(_message.Message):
    __slots__ = ("variationType", "rule", "title", "snippet", "recentChanges", "autoTranslation", "offer", "channelId", "child", "decoration")
    VARIATIONTYPE_FIELD_NUMBER: _ClassVar[int]
    RULE_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    SNIPPET_FIELD_NUMBER: _ClassVar[int]
    RECENTCHANGES_FIELD_NUMBER: _ClassVar[int]
    AUTOTRANSLATION_FIELD_NUMBER: _ClassVar[int]
    OFFER_FIELD_NUMBER: _ClassVar[int]
    CHANNELID_FIELD_NUMBER: _ClassVar[int]
    CHILD_FIELD_NUMBER: _ClassVar[int]
    DECORATION_FIELD_NUMBER: _ClassVar[int]
    variationType: int
    rule: Rule
    title: str
    snippet: _containers.RepeatedScalarFieldContainer[str]
    recentChanges: str
    autoTranslation: _containers.RepeatedCompositeFieldContainer[TranslatedText]
    offer: _containers.RepeatedCompositeFieldContainer[Offer]
    channelId: int
    child: _containers.RepeatedCompositeFieldContainer[Document]
    decoration: _containers.RepeatedCompositeFieldContainer[Document]
    def __init__(self, variationType: _Optional[int] = ..., rule: _Optional[_Union[Rule, _Mapping]] = ..., title: _Optional[str] = ..., snippet: _Optional[_Iterable[str]] = ..., recentChanges: _Optional[str] = ..., autoTranslation: _Optional[_Iterable[_Union[TranslatedText, _Mapping]]] = ..., offer: _Optional[_Iterable[_Union[Offer, _Mapping]]] = ..., channelId: _Optional[int] = ..., child: _Optional[_Iterable[_Union[Document, _Mapping]]] = ..., decoration: _Optional[_Iterable[_Union[Document, _Mapping]]] = ...) -> None: ...

class Image(_message.Message):
    __slots__ = ("imageType", "dimension", "imageUrl", "altTextLocalized", "secureUrl", "positionInSequence", "supportsFifeUrlOptions", "citation", "color", "screenshotSetNumber")
    class Dimension(_message.Message):
        __slots__ = ("width", "height")
        WIDTH_FIELD_NUMBER: _ClassVar[int]
        HEIGHT_FIELD_NUMBER: _ClassVar[int]
        width: int
        height: int
        def __init__(self, width: _Optional[int] = ..., height: _Optional[int] = ...) -> None: ...
    class Citation(_message.Message):
        __slots__ = ("titleLocalized", "url")
        TITLELOCALIZED_FIELD_NUMBER: _ClassVar[int]
        URL_FIELD_NUMBER: _ClassVar[int]
        titleLocalized: str
        url: str
        def __init__(self, titleLocalized: _Optional[str] = ..., url: _Optional[str] = ...) -> None: ...
    IMAGETYPE_FIELD_NUMBER: _ClassVar[int]
    DIMENSION_FIELD_NUMBER: _ClassVar[int]
    IMAGEURL_FIELD_NUMBER: _ClassVar[int]
    ALTTEXTLOCALIZED_FIELD_NUMBER: _ClassVar[int]
    SECUREURL_FIELD_NUMBER: _ClassVar[int]
    POSITIONINSEQUENCE_FIELD_NUMBER: _ClassVar[int]
    SUPPORTSFIFEURLOPTIONS_FIELD_NUMBER: _ClassVar[int]
    CITATION_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    SCREENSHOTSETNUMBER_FIELD_NUMBER: _ClassVar[int]
    imageType: int
    dimension: Image.Dimension
    imageUrl: str
    altTextLocalized: str
    secureUrl: str
    positionInSequence: int
    supportsFifeUrlOptions: bool
    citation: Image.Citation
    color: str
    screenshotSetNumber: int
    def __init__(self, imageType: _Optional[int] = ..., dimension: _Optional[_Union[Image.Dimension, _Mapping]] = ..., imageUrl: _Optional[str] = ..., altTextLocalized: _Optional[str] = ..., secureUrl: _Optional[str] = ..., positionInSequence: _Optional[int] = ..., supportsFifeUrlOptions: _Optional[bool] = ..., citation: _Optional[_Union[Image.Citation, _Mapping]] = ..., color: _Optional[str] = ..., screenshotSetNumber: _Optional[int] = ...) -> None: ...

class TranslatedText(_message.Message):
    __slots__ = ("text", "sourceLocale", "targetLocale")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    SOURCELOCALE_FIELD_NUMBER: _ClassVar[int]
    TARGETLOCALE_FIELD_NUMBER: _ClassVar[int]
    text: str
    sourceLocale: str
    targetLocale: str
    def __init__(self, text: _Optional[str] = ..., sourceLocale: _Optional[str] = ..., targetLocale: _Optional[str] = ...) -> None: ...

class PlusOneData(_message.Message):
    __slots__ = ("setByUser", "total", "circlesTotal", "circlesPeople")
    SETBYUSER_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    CIRCLESTOTAL_FIELD_NUMBER: _ClassVar[int]
    CIRCLESPEOPLE_FIELD_NUMBER: _ClassVar[int]
    setByUser: bool
    total: int
    circlesTotal: int
    circlesPeople: _containers.RepeatedCompositeFieldContainer[PlusPerson]
    def __init__(self, setByUser: _Optional[bool] = ..., total: _Optional[int] = ..., circlesTotal: _Optional[int] = ..., circlesPeople: _Optional[_Iterable[_Union[PlusPerson, _Mapping]]] = ...) -> None: ...

class PlusPerson(_message.Message):
    __slots__ = ("displayName", "profileImageUrl")
    DISPLAYNAME_FIELD_NUMBER: _ClassVar[int]
    PROFILEIMAGEURL_FIELD_NUMBER: _ClassVar[int]
    displayName: str
    profileImageUrl: str
    def __init__(self, displayName: _Optional[str] = ..., profileImageUrl: _Optional[str] = ...) -> None: ...

class AlbumDetails(_message.Message):
    __slots__ = ("name", "details", "displayArtist")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    DISPLAYARTIST_FIELD_NUMBER: _ClassVar[int]
    name: str
    details: MusicDetails
    displayArtist: ArtistDetails
    def __init__(self, name: _Optional[str] = ..., details: _Optional[_Union[MusicDetails, _Mapping]] = ..., displayArtist: _Optional[_Union[ArtistDetails, _Mapping]] = ...) -> None: ...

class AppDetails(_message.Message):
    __slots__ = ("developerName", "majorVersionNumber", "versionCode", "versionString", "title", "appCategory", "contentRating", "installationSize", "permission", "developerEmail", "developerWebsite", "numDownloads", "packageName", "recentChangesHtml", "uploadDate", "file", "appType", "unstable", "hasInstantLink", "containsAds", "dependencies", "testingProgramInfo", "earlyAccessInfo", "instantLink", "developerAddress")
    DEVELOPERNAME_FIELD_NUMBER: _ClassVar[int]
    MAJORVERSIONNUMBER_FIELD_NUMBER: _ClassVar[int]
    VERSIONCODE_FIELD_NUMBER: _ClassVar[int]
    VERSIONSTRING_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    APPCATEGORY_FIELD_NUMBER: _ClassVar[int]
    CONTENTRATING_FIELD_NUMBER: _ClassVar[int]
    INSTALLATIONSIZE_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_FIELD_NUMBER: _ClassVar[int]
    DEVELOPEREMAIL_FIELD_NUMBER: _ClassVar[int]
    DEVELOPERWEBSITE_FIELD_NUMBER: _ClassVar[int]
    NUMDOWNLOADS_FIELD_NUMBER: _ClassVar[int]
    PACKAGENAME_FIELD_NUMBER: _ClassVar[int]
    RECENTCHANGESHTML_FIELD_NUMBER: _ClassVar[int]
    UPLOADDATE_FIELD_NUMBER: _ClassVar[int]
    FILE_FIELD_NUMBER: _ClassVar[int]
    APPTYPE_FIELD_NUMBER: _ClassVar[int]
    UNSTABLE_FIELD_NUMBER: _ClassVar[int]
    HASINSTANTLINK_FIELD_NUMBER: _ClassVar[int]
    CONTAINSADS_FIELD_NUMBER: _ClassVar[int]
    DEPENDENCIES_FIELD_NUMBER: _ClassVar[int]
    TESTINGPROGRAMINFO_FIELD_NUMBER: _ClassVar[int]
    EARLYACCESSINFO_FIELD_NUMBER: _ClassVar[int]
    INSTANTLINK_FIELD_NUMBER: _ClassVar[int]
    DEVELOPERADDRESS_FIELD_NUMBER: _ClassVar[int]
    developerName: str
    majorVersionNumber: int
    versionCode: int
    versionString: str
    title: str
    appCategory: _containers.RepeatedScalarFieldContainer[str]
    contentRating: int
    installationSize: int
    permission: _containers.RepeatedScalarFieldContainer[str]
    developerEmail: str
    developerWebsite: str
    numDownloads: str
    packageName: str
    recentChangesHtml: str
    uploadDate: str
    file: _containers.RepeatedCompositeFieldContainer[FileMetadata]
    appType: str
    unstable: bool
    hasInstantLink: bool
    containsAds: str
    dependencies: Dependencies
    testingProgramInfo: TestingProgramInfo
    earlyAccessInfo: EarlyAccessInfo
    instantLink: str
    developerAddress: str
    def __init__(self, developerName: _Optional[str] = ..., majorVersionNumber: _Optional[int] = ..., versionCode: _Optional[int] = ..., versionString: _Optional[str] = ..., title: _Optional[str] = ..., appCategory: _Optional[_Iterable[str]] = ..., contentRating: _Optional[int] = ..., installationSize: _Optional[int] = ..., permission: _Optional[_Iterable[str]] = ..., developerEmail: _Optional[str] = ..., developerWebsite: _Optional[str] = ..., numDownloads: _Optional[str] = ..., packageName: _Optional[str] = ..., recentChangesHtml: _Optional[str] = ..., uploadDate: _Optional[str] = ..., file: _Optional[_Iterable[_Union[FileMetadata, _Mapping]]] = ..., appType: _Optional[str] = ..., unstable: _Optional[bool] = ..., hasInstantLink: _Optional[bool] = ..., containsAds: _Optional[str] = ..., dependencies: _Optional[_Union[Dependencies, _Mapping]] = ..., testingProgramInfo: _Optional[_Union[TestingProgramInfo, _Mapping]] = ..., earlyAccessInfo: _Optional[_Union[EarlyAccessInfo, _Mapping]] = ..., instantLink: _Optional[str] = ..., developerAddress: _Optional[str] = ...) -> None: ...

class Dependencies(_message.Message):
    __slots__ = ("unknown1", "unknown2", "dependency", "unknown3")
    UNKNOWN1_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN2_FIELD_NUMBER: _ClassVar[int]
    DEPENDENCY_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN3_FIELD_NUMBER: _ClassVar[int]
    unknown1: int
    unknown2: int
    dependency: _containers.RepeatedCompositeFieldContainer[Dependency]
    unknown3: int
    def __init__(self, unknown1: _Optional[int] = ..., unknown2: _Optional[int] = ..., dependency: _Optional[_Iterable[_Union[Dependency, _Mapping]]] = ..., unknown3: _Optional[int] = ...) -> None: ...

class Dependency(_message.Message):
    __slots__ = ("packageName", "version", "unknown4")
    PACKAGENAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN4_FIELD_NUMBER: _ClassVar[int]
    packageName: str
    version: int
    unknown4: int
    def __init__(self, packageName: _Optional[str] = ..., version: _Optional[int] = ..., unknown4: _Optional[int] = ...) -> None: ...

class TestingProgramInfo(_message.Message):
    __slots__ = ("subscribed", "subscribed1", "testingProgramEmail")
    SUBSCRIBED_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIBED1_FIELD_NUMBER: _ClassVar[int]
    TESTINGPROGRAMEMAIL_FIELD_NUMBER: _ClassVar[int]
    subscribed: bool
    subscribed1: bool
    testingProgramEmail: str
    def __init__(self, subscribed: _Optional[bool] = ..., subscribed1: _Optional[bool] = ..., testingProgramEmail: _Optional[str] = ...) -> None: ...

class EarlyAccessInfo(_message.Message):
    __slots__ = ("email",)
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    email: str
    def __init__(self, email: _Optional[str] = ...) -> None: ...

class ArtistDetails(_message.Message):
    __slots__ = ("detailsUrl", "name", "externalLinks")
    DETAILSURL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EXTERNALLINKS_FIELD_NUMBER: _ClassVar[int]
    detailsUrl: str
    name: str
    externalLinks: ArtistExternalLinks
    def __init__(self, detailsUrl: _Optional[str] = ..., name: _Optional[str] = ..., externalLinks: _Optional[_Union[ArtistExternalLinks, _Mapping]] = ...) -> None: ...

class ArtistExternalLinks(_message.Message):
    __slots__ = ("websiteUrl", "googlePlusProfileUrl", "youtubeChannelUrl")
    WEBSITEURL_FIELD_NUMBER: _ClassVar[int]
    GOOGLEPLUSPROFILEURL_FIELD_NUMBER: _ClassVar[int]
    YOUTUBECHANNELURL_FIELD_NUMBER: _ClassVar[int]
    websiteUrl: _containers.RepeatedScalarFieldContainer[str]
    googlePlusProfileUrl: str
    youtubeChannelUrl: str
    def __init__(self, websiteUrl: _Optional[_Iterable[str]] = ..., googlePlusProfileUrl: _Optional[str] = ..., youtubeChannelUrl: _Optional[str] = ...) -> None: ...

class DocumentDetails(_message.Message):
    __slots__ = ("appDetails", "albumDetails", "artistDetails", "songDetails", "bookDetails", "videoDetails", "subscriptionDetails", "magazineDetails", "tvShowDetails", "tvSeasonDetails", "tvEpisodeDetails")
    APPDETAILS_FIELD_NUMBER: _ClassVar[int]
    ALBUMDETAILS_FIELD_NUMBER: _ClassVar[int]
    ARTISTDETAILS_FIELD_NUMBER: _ClassVar[int]
    SONGDETAILS_FIELD_NUMBER: _ClassVar[int]
    BOOKDETAILS_FIELD_NUMBER: _ClassVar[int]
    VIDEODETAILS_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTIONDETAILS_FIELD_NUMBER: _ClassVar[int]
    MAGAZINEDETAILS_FIELD_NUMBER: _ClassVar[int]
    TVSHOWDETAILS_FIELD_NUMBER: _ClassVar[int]
    TVSEASONDETAILS_FIELD_NUMBER: _ClassVar[int]
    TVEPISODEDETAILS_FIELD_NUMBER: _ClassVar[int]
    appDetails: AppDetails
    albumDetails: AlbumDetails
    artistDetails: ArtistDetails
    songDetails: SongDetails
    bookDetails: BookDetails
    videoDetails: VideoDetails
    subscriptionDetails: SubscriptionDetails
    magazineDetails: MagazineDetails
    tvShowDetails: TvShowDetails
    tvSeasonDetails: TvSeasonDetails
    tvEpisodeDetails: TvEpisodeDetails
    def __init__(self, appDetails: _Optional[_Union[AppDetails, _Mapping]] = ..., albumDetails: _Optional[_Union[AlbumDetails, _Mapping]] = ..., artistDetails: _Optional[_Union[ArtistDetails, _Mapping]] = ..., songDetails: _Optional[_Union[SongDetails, _Mapping]] = ..., bookDetails: _Optional[_Union[BookDetails, _Mapping]] = ..., videoDetails: _Optional[_Union[VideoDetails, _Mapping]] = ..., subscriptionDetails: _Optional[_Union[SubscriptionDetails, _Mapping]] = ..., magazineDetails: _Optional[_Union[MagazineDetails, _Mapping]] = ..., tvShowDetails: _Optional[_Union[TvShowDetails, _Mapping]] = ..., tvSeasonDetails: _Optional[_Union[TvSeasonDetails, _Mapping]] = ..., tvEpisodeDetails: _Optional[_Union[TvEpisodeDetails, _Mapping]] = ...) -> None: ...

class FileMetadata(_message.Message):
    __slots__ = ("fileType", "versionCode", "size")
    FILETYPE_FIELD_NUMBER: _ClassVar[int]
    VERSIONCODE_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    fileType: int
    versionCode: int
    size: int
    def __init__(self, fileType: _Optional[int] = ..., versionCode: _Optional[int] = ..., size: _Optional[int] = ...) -> None: ...

class MagazineDetails(_message.Message):
    __slots__ = ("parentDetailsUrl", "deviceAvailabilityDescriptionHtml", "psvDescription", "deliveryFrequencyDescription")
    PARENTDETAILSURL_FIELD_NUMBER: _ClassVar[int]
    DEVICEAVAILABILITYDESCRIPTIONHTML_FIELD_NUMBER: _ClassVar[int]
    PSVDESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DELIVERYFREQUENCYDESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    parentDetailsUrl: str
    deviceAvailabilityDescriptionHtml: str
    psvDescription: str
    deliveryFrequencyDescription: str
    def __init__(self, parentDetailsUrl: _Optional[str] = ..., deviceAvailabilityDescriptionHtml: _Optional[str] = ..., psvDescription: _Optional[str] = ..., deliveryFrequencyDescription: _Optional[str] = ...) -> None: ...

class MusicDetails(_message.Message):
    __slots__ = ("censoring", "durationSec", "originalReleaseDate", "label", "artist", "genre", "releaseDate", "releaseType")
    CENSORING_FIELD_NUMBER: _ClassVar[int]
    DURATIONSEC_FIELD_NUMBER: _ClassVar[int]
    ORIGINALRELEASEDATE_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    ARTIST_FIELD_NUMBER: _ClassVar[int]
    GENRE_FIELD_NUMBER: _ClassVar[int]
    RELEASEDATE_FIELD_NUMBER: _ClassVar[int]
    RELEASETYPE_FIELD_NUMBER: _ClassVar[int]
    censoring: int
    durationSec: int
    originalReleaseDate: str
    label: str
    artist: _containers.RepeatedCompositeFieldContainer[ArtistDetails]
    genre: _containers.RepeatedScalarFieldContainer[str]
    releaseDate: str
    releaseType: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, censoring: _Optional[int] = ..., durationSec: _Optional[int] = ..., originalReleaseDate: _Optional[str] = ..., label: _Optional[str] = ..., artist: _Optional[_Iterable[_Union[ArtistDetails, _Mapping]]] = ..., genre: _Optional[_Iterable[str]] = ..., releaseDate: _Optional[str] = ..., releaseType: _Optional[_Iterable[int]] = ...) -> None: ...

class SongDetails(_message.Message):
    __slots__ = ("name", "details", "albumName", "trackNumber", "previewUrl", "displayArtist")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    ALBUMNAME_FIELD_NUMBER: _ClassVar[int]
    TRACKNUMBER_FIELD_NUMBER: _ClassVar[int]
    PREVIEWURL_FIELD_NUMBER: _ClassVar[int]
    DISPLAYARTIST_FIELD_NUMBER: _ClassVar[int]
    name: str
    details: MusicDetails
    albumName: str
    trackNumber: int
    previewUrl: str
    displayArtist: ArtistDetails
    def __init__(self, name: _Optional[str] = ..., details: _Optional[_Union[MusicDetails, _Mapping]] = ..., albumName: _Optional[str] = ..., trackNumber: _Optional[int] = ..., previewUrl: _Optional[str] = ..., displayArtist: _Optional[_Union[ArtistDetails, _Mapping]] = ...) -> None: ...

class SubscriptionDetails(_message.Message):
    __slots__ = ("subscriptionPeriod",)
    SUBSCRIPTIONPERIOD_FIELD_NUMBER: _ClassVar[int]
    subscriptionPeriod: int
    def __init__(self, subscriptionPeriod: _Optional[int] = ...) -> None: ...

class Trailer(_message.Message):
    __slots__ = ("trailerId", "title", "thumbnailUrl", "watchUrl", "duration")
    TRAILERID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    THUMBNAILURL_FIELD_NUMBER: _ClassVar[int]
    WATCHURL_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    trailerId: str
    title: str
    thumbnailUrl: str
    watchUrl: str
    duration: str
    def __init__(self, trailerId: _Optional[str] = ..., title: _Optional[str] = ..., thumbnailUrl: _Optional[str] = ..., watchUrl: _Optional[str] = ..., duration: _Optional[str] = ...) -> None: ...

class TvEpisodeDetails(_message.Message):
    __slots__ = ("parentDetailsUrl", "episodeIndex", "releaseDate")
    PARENTDETAILSURL_FIELD_NUMBER: _ClassVar[int]
    EPISODEINDEX_FIELD_NUMBER: _ClassVar[int]
    RELEASEDATE_FIELD_NUMBER: _ClassVar[int]
    parentDetailsUrl: str
    episodeIndex: int
    releaseDate: str
    def __init__(self, parentDetailsUrl: _Optional[str] = ..., episodeIndex: _Optional[int] = ..., releaseDate: _Optional[str] = ...) -> None: ...

class TvSeasonDetails(_message.Message):
    __slots__ = ("parentDetailsUrl", "seasonIndex", "releaseDate", "broadcaster")
    PARENTDETAILSURL_FIELD_NUMBER: _ClassVar[int]
    SEASONINDEX_FIELD_NUMBER: _ClassVar[int]
    RELEASEDATE_FIELD_NUMBER: _ClassVar[int]
    BROADCASTER_FIELD_NUMBER: _ClassVar[int]
    parentDetailsUrl: str
    seasonIndex: int
    releaseDate: str
    broadcaster: str
    def __init__(self, parentDetailsUrl: _Optional[str] = ..., seasonIndex: _Optional[int] = ..., releaseDate: _Optional[str] = ..., broadcaster: _Optional[str] = ...) -> None: ...

class TvShowDetails(_message.Message):
    __slots__ = ("seasonCount", "startYear", "endYear", "broadcaster")
    SEASONCOUNT_FIELD_NUMBER: _ClassVar[int]
    STARTYEAR_FIELD_NUMBER: _ClassVar[int]
    ENDYEAR_FIELD_NUMBER: _ClassVar[int]
    BROADCASTER_FIELD_NUMBER: _ClassVar[int]
    seasonCount: int
    startYear: int
    endYear: int
    broadcaster: str
    def __init__(self, seasonCount: _Optional[int] = ..., startYear: _Optional[int] = ..., endYear: _Optional[int] = ..., broadcaster: _Optional[str] = ...) -> None: ...

class VideoCredit(_message.Message):
    __slots__ = ("creditType", "credit", "name")
    CREDITTYPE_FIELD_NUMBER: _ClassVar[int]
    CREDIT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    creditType: int
    credit: str
    name: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, creditType: _Optional[int] = ..., credit: _Optional[str] = ..., name: _Optional[_Iterable[str]] = ...) -> None: ...

class VideoDetails(_message.Message):
    __slots__ = ("credit", "duration", "releaseDate", "contentRating", "likes", "dislikes", "genre", "trailer", "rentalTerm")
    CREDIT_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    RELEASEDATE_FIELD_NUMBER: _ClassVar[int]
    CONTENTRATING_FIELD_NUMBER: _ClassVar[int]
    LIKES_FIELD_NUMBER: _ClassVar[int]
    DISLIKES_FIELD_NUMBER: _ClassVar[int]
    GENRE_FIELD_NUMBER: _ClassVar[int]
    TRAILER_FIELD_NUMBER: _ClassVar[int]
    RENTALTERM_FIELD_NUMBER: _ClassVar[int]
    credit: _containers.RepeatedCompositeFieldContainer[VideoCredit]
    duration: str
    releaseDate: str
    contentRating: str
    likes: int
    dislikes: int
    genre: _containers.RepeatedScalarFieldContainer[str]
    trailer: _containers.RepeatedCompositeFieldContainer[Trailer]
    rentalTerm: _containers.RepeatedCompositeFieldContainer[VideoRentalTerm]
    def __init__(self, credit: _Optional[_Iterable[_Union[VideoCredit, _Mapping]]] = ..., duration: _Optional[str] = ..., releaseDate: _Optional[str] = ..., contentRating: _Optional[str] = ..., likes: _Optional[int] = ..., dislikes: _Optional[int] = ..., genre: _Optional[_Iterable[str]] = ..., trailer: _Optional[_Iterable[_Union[Trailer, _Mapping]]] = ..., rentalTerm: _Optional[_Iterable[_Union[VideoRentalTerm, _Mapping]]] = ...) -> None: ...

class VideoRentalTerm(_message.Message):
    __slots__ = ("offerType", "offerAbbreviation", "rentalHeader", "term")
    class Term(_message.Message):
        __slots__ = ("header", "body")
        HEADER_FIELD_NUMBER: _ClassVar[int]
        BODY_FIELD_NUMBER: _ClassVar[int]
        header: str
        body: str
        def __init__(self, header: _Optional[str] = ..., body: _Optional[str] = ...) -> None: ...
    OFFERTYPE_FIELD_NUMBER: _ClassVar[int]
    OFFERABBREVIATION_FIELD_NUMBER: _ClassVar[int]
    RENTALHEADER_FIELD_NUMBER: _ClassVar[int]
    TERM_FIELD_NUMBER: _ClassVar[int]
    offerType: int
    offerAbbreviation: str
    rentalHeader: str
    term: _containers.RepeatedCompositeFieldContainer[VideoRentalTerm.Term]
    def __init__(self, offerType: _Optional[int] = ..., offerAbbreviation: _Optional[str] = ..., rentalHeader: _Optional[str] = ..., term: _Optional[_Iterable[_Union[VideoRentalTerm.Term, _Mapping]]] = ...) -> None: ...

class Bucket(_message.Message):
    __slots__ = ("document", "multiCorpus", "title", "iconUrl", "fullContentsUrl", "relevance", "estimatedResults", "analyticsCookie", "fullContentsListUrl", "nextPageUrl", "ordered")
    DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    MULTICORPUS_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    ICONURL_FIELD_NUMBER: _ClassVar[int]
    FULLCONTENTSURL_FIELD_NUMBER: _ClassVar[int]
    RELEVANCE_FIELD_NUMBER: _ClassVar[int]
    ESTIMATEDRESULTS_FIELD_NUMBER: _ClassVar[int]
    ANALYTICSCOOKIE_FIELD_NUMBER: _ClassVar[int]
    FULLCONTENTSLISTURL_FIELD_NUMBER: _ClassVar[int]
    NEXTPAGEURL_FIELD_NUMBER: _ClassVar[int]
    ORDERED_FIELD_NUMBER: _ClassVar[int]
    document: _containers.RepeatedCompositeFieldContainer[DocV1]
    multiCorpus: bool
    title: str
    iconUrl: str
    fullContentsUrl: str
    relevance: float
    estimatedResults: int
    analyticsCookie: str
    fullContentsListUrl: str
    nextPageUrl: str
    ordered: bool
    def __init__(self, document: _Optional[_Iterable[_Union[DocV1, _Mapping]]] = ..., multiCorpus: _Optional[bool] = ..., title: _Optional[str] = ..., iconUrl: _Optional[str] = ..., fullContentsUrl: _Optional[str] = ..., relevance: _Optional[float] = ..., estimatedResults: _Optional[int] = ..., analyticsCookie: _Optional[str] = ..., fullContentsListUrl: _Optional[str] = ..., nextPageUrl: _Optional[str] = ..., ordered: _Optional[bool] = ...) -> None: ...

class ListResponse(_message.Message):
    __slots__ = ("bucket", "doc")
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    DOC_FIELD_NUMBER: _ClassVar[int]
    bucket: _containers.RepeatedCompositeFieldContainer[Bucket]
    doc: _containers.RepeatedCompositeFieldContainer[DocV2]
    def __init__(self, bucket: _Optional[_Iterable[_Union[Bucket, _Mapping]]] = ..., doc: _Optional[_Iterable[_Union[DocV2, _Mapping]]] = ...) -> None: ...

class DocV1(_message.Message):
    __slots__ = ("finskyDoc", "docid", "detailsUrl", "reviewsUrl", "relatedListUrl", "moreByListUrl", "shareUrl", "creator", "details", "descriptionHtml", "relatedBrowseUrl", "moreByBrowseUrl", "relatedHeader", "moreByHeader", "title", "plusOneData", "warningMessage")
    FINSKYDOC_FIELD_NUMBER: _ClassVar[int]
    DOCID_FIELD_NUMBER: _ClassVar[int]
    DETAILSURL_FIELD_NUMBER: _ClassVar[int]
    REVIEWSURL_FIELD_NUMBER: _ClassVar[int]
    RELATEDLISTURL_FIELD_NUMBER: _ClassVar[int]
    MOREBYLISTURL_FIELD_NUMBER: _ClassVar[int]
    SHAREURL_FIELD_NUMBER: _ClassVar[int]
    CREATOR_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTIONHTML_FIELD_NUMBER: _ClassVar[int]
    RELATEDBROWSEURL_FIELD_NUMBER: _ClassVar[int]
    MOREBYBROWSEURL_FIELD_NUMBER: _ClassVar[int]
    RELATEDHEADER_FIELD_NUMBER: _ClassVar[int]
    MOREBYHEADER_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    PLUSONEDATA_FIELD_NUMBER: _ClassVar[int]
    WARNINGMESSAGE_FIELD_NUMBER: _ClassVar[int]
    finskyDoc: Document
    docid: str
    detailsUrl: str
    reviewsUrl: str
    relatedListUrl: str
    moreByListUrl: str
    shareUrl: str
    creator: str
    details: DocumentDetails
    descriptionHtml: str
    relatedBrowseUrl: str
    moreByBrowseUrl: str
    relatedHeader: str
    moreByHeader: str
    title: str
    plusOneData: PlusOneData
    warningMessage: str
    def __init__(self, finskyDoc: _Optional[_Union[Document, _Mapping]] = ..., docid: _Optional[str] = ..., detailsUrl: _Optional[str] = ..., reviewsUrl: _Optional[str] = ..., relatedListUrl: _Optional[str] = ..., moreByListUrl: _Optional[str] = ..., shareUrl: _Optional[str] = ..., creator: _Optional[str] = ..., details: _Optional[_Union[DocumentDetails, _Mapping]] = ..., descriptionHtml: _Optional[str] = ..., relatedBrowseUrl: _Optional[str] = ..., moreByBrowseUrl: _Optional[str] = ..., relatedHeader: _Optional[str] = ..., moreByHeader: _Optional[str] = ..., title: _Optional[str] = ..., plusOneData: _Optional[_Union[PlusOneData, _Mapping]] = ..., warningMessage: _Optional[str] = ...) -> None: ...

class DocV2(_message.Message):
    __slots__ = ("docid", "backendDocid", "docType", "backendId", "title", "creator", "descriptionHtml", "offer", "availability", "image", "child", "containerMetadata", "details", "aggregateRating", "relatedLinks", "detailsUrl", "shareUrl", "reviewsUrl", "backendUrl", "purchaseDetailsUrl", "detailsReusable", "subtitle", "unknownCategoryContainer", "unknown25", "descriptionShort", "reviewSnippetsUrl", "reviewQuestionsUrl")
    DOCID_FIELD_NUMBER: _ClassVar[int]
    BACKENDDOCID_FIELD_NUMBER: _ClassVar[int]
    DOCTYPE_FIELD_NUMBER: _ClassVar[int]
    BACKENDID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    CREATOR_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTIONHTML_FIELD_NUMBER: _ClassVar[int]
    OFFER_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    CHILD_FIELD_NUMBER: _ClassVar[int]
    CONTAINERMETADATA_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    AGGREGATERATING_FIELD_NUMBER: _ClassVar[int]
    RELATEDLINKS_FIELD_NUMBER: _ClassVar[int]
    DETAILSURL_FIELD_NUMBER: _ClassVar[int]
    SHAREURL_FIELD_NUMBER: _ClassVar[int]
    REVIEWSURL_FIELD_NUMBER: _ClassVar[int]
    BACKENDURL_FIELD_NUMBER: _ClassVar[int]
    PURCHASEDETAILSURL_FIELD_NUMBER: _ClassVar[int]
    DETAILSREUSABLE_FIELD_NUMBER: _ClassVar[int]
    SUBTITLE_FIELD_NUMBER: _ClassVar[int]
    UNKNOWNCATEGORYCONTAINER_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN25_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTIONSHORT_FIELD_NUMBER: _ClassVar[int]
    REVIEWSNIPPETSURL_FIELD_NUMBER: _ClassVar[int]
    REVIEWQUESTIONSURL_FIELD_NUMBER: _ClassVar[int]
    docid: str
    backendDocid: str
    docType: int
    backendId: int
    title: str
    creator: str
    descriptionHtml: str
    offer: _containers.RepeatedCompositeFieldContainer[Offer]
    availability: Availability
    image: _containers.RepeatedCompositeFieldContainer[Image]
    child: _containers.RepeatedCompositeFieldContainer[DocV2]
    containerMetadata: ContainerMetadata
    details: DocumentDetails
    aggregateRating: AggregateRating
    relatedLinks: RelatedLinks
    detailsUrl: str
    shareUrl: str
    reviewsUrl: str
    backendUrl: str
    purchaseDetailsUrl: str
    detailsReusable: bool
    subtitle: str
    unknownCategoryContainer: UnknownCategoryContainer
    unknown25: Unknown25
    descriptionShort: str
    reviewSnippetsUrl: str
    reviewQuestionsUrl: str
    def __init__(self, docid: _Optional[str] = ..., backendDocid: _Optional[str] = ..., docType: _Optional[int] = ..., backendId: _Optional[int] = ..., title: _Optional[str] = ..., creator: _Optional[str] = ..., descriptionHtml: _Optional[str] = ..., offer: _Optional[_Iterable[_Union[Offer, _Mapping]]] = ..., availability: _Optional[_Union[Availability, _Mapping]] = ..., image: _Optional[_Iterable[_Union[Image, _Mapping]]] = ..., child: _Optional[_Iterable[_Union[DocV2, _Mapping]]] = ..., containerMetadata: _Optional[_Union[ContainerMetadata, _Mapping]] = ..., details: _Optional[_Union[DocumentDetails, _Mapping]] = ..., aggregateRating: _Optional[_Union[AggregateRating, _Mapping]] = ..., relatedLinks: _Optional[_Union[RelatedLinks, _Mapping]] = ..., detailsUrl: _Optional[str] = ..., shareUrl: _Optional[str] = ..., reviewsUrl: _Optional[str] = ..., backendUrl: _Optional[str] = ..., purchaseDetailsUrl: _Optional[str] = ..., detailsReusable: _Optional[bool] = ..., subtitle: _Optional[str] = ..., unknownCategoryContainer: _Optional[_Union[UnknownCategoryContainer, _Mapping]] = ..., unknown25: _Optional[_Union[Unknown25, _Mapping]] = ..., descriptionShort: _Optional[str] = ..., reviewSnippetsUrl: _Optional[str] = ..., reviewQuestionsUrl: _Optional[str] = ...) -> None: ...

class Unknown25(_message.Message):
    __slots__ = ("item",)
    ITEM_FIELD_NUMBER: _ClassVar[int]
    item: _containers.RepeatedCompositeFieldContainer[Unknown25Item]
    def __init__(self, item: _Optional[_Iterable[_Union[Unknown25Item, _Mapping]]] = ...) -> None: ...

class Unknown25Item(_message.Message):
    __slots__ = ("label", "container")
    LABEL_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_FIELD_NUMBER: _ClassVar[int]
    label: str
    container: Unknown25Container
    def __init__(self, label: _Optional[str] = ..., container: _Optional[_Union[Unknown25Container, _Mapping]] = ...) -> None: ...

class Unknown25Container(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str
    def __init__(self, value: _Optional[str] = ...) -> None: ...

class RelatedLinks(_message.Message):
    __slots__ = ("unknown1", "privacyPolicyUrl", "youMightAlsoLike", "rated", "relatedLinks", "categoryInfo")
    UNKNOWN1_FIELD_NUMBER: _ClassVar[int]
    PRIVACYPOLICYURL_FIELD_NUMBER: _ClassVar[int]
    YOUMIGHTALSOLIKE_FIELD_NUMBER: _ClassVar[int]
    RATED_FIELD_NUMBER: _ClassVar[int]
    RELATEDLINKS_FIELD_NUMBER: _ClassVar[int]
    CATEGORYINFO_FIELD_NUMBER: _ClassVar[int]
    unknown1: RelatedLinksUnknown1
    privacyPolicyUrl: str
    youMightAlsoLike: RelatedLink
    rated: Rated
    relatedLinks: _containers.RepeatedCompositeFieldContainer[RelatedLink]
    categoryInfo: CategoryInfo
    def __init__(self, unknown1: _Optional[_Union[RelatedLinksUnknown1, _Mapping]] = ..., privacyPolicyUrl: _Optional[str] = ..., youMightAlsoLike: _Optional[_Union[RelatedLink, _Mapping]] = ..., rated: _Optional[_Union[Rated, _Mapping]] = ..., relatedLinks: _Optional[_Iterable[_Union[RelatedLink, _Mapping]]] = ..., categoryInfo: _Optional[_Union[CategoryInfo, _Mapping]] = ...) -> None: ...

class RelatedLinksUnknown1(_message.Message):
    __slots__ = ("unknown2",)
    UNKNOWN2_FIELD_NUMBER: _ClassVar[int]
    unknown2: RelatedLinksUnknown2
    def __init__(self, unknown2: _Optional[_Union[RelatedLinksUnknown2, _Mapping]] = ...) -> None: ...

class RelatedLinksUnknown2(_message.Message):
    __slots__ = ("homeUrl", "nextPageUrl")
    HOMEURL_FIELD_NUMBER: _ClassVar[int]
    NEXTPAGEURL_FIELD_NUMBER: _ClassVar[int]
    homeUrl: str
    nextPageUrl: str
    def __init__(self, homeUrl: _Optional[str] = ..., nextPageUrl: _Optional[str] = ...) -> None: ...

class Rated(_message.Message):
    __slots__ = ("label", "image", "learnMoreHtmlLink")
    LABEL_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    LEARNMOREHTMLLINK_FIELD_NUMBER: _ClassVar[int]
    label: str
    image: Image
    learnMoreHtmlLink: str
    def __init__(self, label: _Optional[str] = ..., image: _Optional[_Union[Image, _Mapping]] = ..., learnMoreHtmlLink: _Optional[str] = ...) -> None: ...

class RelatedLink(_message.Message):
    __slots__ = ("label", "url1", "url2")
    LABEL_FIELD_NUMBER: _ClassVar[int]
    URL1_FIELD_NUMBER: _ClassVar[int]
    URL2_FIELD_NUMBER: _ClassVar[int]
    label: str
    url1: str
    url2: str
    def __init__(self, label: _Optional[str] = ..., url1: _Optional[str] = ..., url2: _Optional[str] = ...) -> None: ...

class CategoryInfo(_message.Message):
    __slots__ = ("appType", "appCategory")
    APPTYPE_FIELD_NUMBER: _ClassVar[int]
    APPCATEGORY_FIELD_NUMBER: _ClassVar[int]
    appType: str
    appCategory: str
    def __init__(self, appType: _Optional[str] = ..., appCategory: _Optional[str] = ...) -> None: ...

class EncryptedSubscriberInfo(_message.Message):
    __slots__ = ("data", "encryptedKey", "signature", "initVector", "googleKeyVersion", "carrierKeyVersion")
    DATA_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTEDKEY_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    INITVECTOR_FIELD_NUMBER: _ClassVar[int]
    GOOGLEKEYVERSION_FIELD_NUMBER: _ClassVar[int]
    CARRIERKEYVERSION_FIELD_NUMBER: _ClassVar[int]
    data: str
    encryptedKey: str
    signature: str
    initVector: str
    googleKeyVersion: int
    carrierKeyVersion: int
    def __init__(self, data: _Optional[str] = ..., encryptedKey: _Optional[str] = ..., signature: _Optional[str] = ..., initVector: _Optional[str] = ..., googleKeyVersion: _Optional[int] = ..., carrierKeyVersion: _Optional[int] = ...) -> None: ...

class Availability(_message.Message):
    __slots__ = ("restriction", "offerType", "rule", "perdeviceavailabilityrestriction", "availableIfOwned", "install", "filterInfo", "ownershipInfo")
    class PerDeviceAvailabilityRestriction(_message.Message):
        __slots__ = ("androidId", "deviceRestriction", "channelId", "filterInfo")
        ANDROIDID_FIELD_NUMBER: _ClassVar[int]
        DEVICERESTRICTION_FIELD_NUMBER: _ClassVar[int]
        CHANNELID_FIELD_NUMBER: _ClassVar[int]
        FILTERINFO_FIELD_NUMBER: _ClassVar[int]
        androidId: int
        deviceRestriction: int
        channelId: int
        filterInfo: FilterEvaluationInfo
        def __init__(self, androidId: _Optional[int] = ..., deviceRestriction: _Optional[int] = ..., channelId: _Optional[int] = ..., filterInfo: _Optional[_Union[FilterEvaluationInfo, _Mapping]] = ...) -> None: ...
    RESTRICTION_FIELD_NUMBER: _ClassVar[int]
    OFFERTYPE_FIELD_NUMBER: _ClassVar[int]
    RULE_FIELD_NUMBER: _ClassVar[int]
    PERDEVICEAVAILABILITYRESTRICTION_FIELD_NUMBER: _ClassVar[int]
    AVAILABLEIFOWNED_FIELD_NUMBER: _ClassVar[int]
    INSTALL_FIELD_NUMBER: _ClassVar[int]
    FILTERINFO_FIELD_NUMBER: _ClassVar[int]
    OWNERSHIPINFO_FIELD_NUMBER: _ClassVar[int]
    restriction: int
    offerType: int
    rule: Rule
    perdeviceavailabilityrestriction: _containers.RepeatedCompositeFieldContainer[Availability.PerDeviceAvailabilityRestriction]
    availableIfOwned: bool
    install: _containers.RepeatedCompositeFieldContainer[Install]
    filterInfo: FilterEvaluationInfo
    ownershipInfo: OwnershipInfo
    def __init__(self, restriction: _Optional[int] = ..., offerType: _Optional[int] = ..., rule: _Optional[_Union[Rule, _Mapping]] = ..., perdeviceavailabilityrestriction: _Optional[_Iterable[_Union[Availability.PerDeviceAvailabilityRestriction, _Mapping]]] = ..., availableIfOwned: _Optional[bool] = ..., install: _Optional[_Iterable[_Union[Install, _Mapping]]] = ..., filterInfo: _Optional[_Union[FilterEvaluationInfo, _Mapping]] = ..., ownershipInfo: _Optional[_Union[OwnershipInfo, _Mapping]] = ...) -> None: ...

class FilterEvaluationInfo(_message.Message):
    __slots__ = ("ruleEvaluation",)
    RULEEVALUATION_FIELD_NUMBER: _ClassVar[int]
    ruleEvaluation: _containers.RepeatedCompositeFieldContainer[RuleEvaluation]
    def __init__(self, ruleEvaluation: _Optional[_Iterable[_Union[RuleEvaluation, _Mapping]]] = ...) -> None: ...

class Rule(_message.Message):
    __slots__ = ("negate", "operator", "key", "stringArg", "longArg", "doubleArg", "subrule", "responseCode", "comment", "stringArgHash", "constArg")
    NEGATE_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    STRINGARG_FIELD_NUMBER: _ClassVar[int]
    LONGARG_FIELD_NUMBER: _ClassVar[int]
    DOUBLEARG_FIELD_NUMBER: _ClassVar[int]
    SUBRULE_FIELD_NUMBER: _ClassVar[int]
    RESPONSECODE_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    STRINGARGHASH_FIELD_NUMBER: _ClassVar[int]
    CONSTARG_FIELD_NUMBER: _ClassVar[int]
    negate: bool
    operator: int
    key: int
    stringArg: _containers.RepeatedScalarFieldContainer[str]
    longArg: _containers.RepeatedScalarFieldContainer[int]
    doubleArg: _containers.RepeatedScalarFieldContainer[float]
    subrule: _containers.RepeatedCompositeFieldContainer[Rule]
    responseCode: int
    comment: str
    stringArgHash: _containers.RepeatedScalarFieldContainer[int]
    constArg: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, negate: _Optional[bool] = ..., operator: _Optional[int] = ..., key: _Optional[int] = ..., stringArg: _Optional[_Iterable[str]] = ..., longArg: _Optional[_Iterable[int]] = ..., doubleArg: _Optional[_Iterable[float]] = ..., subrule: _Optional[_Iterable[_Union[Rule, _Mapping]]] = ..., responseCode: _Optional[int] = ..., comment: _Optional[str] = ..., stringArgHash: _Optional[_Iterable[int]] = ..., constArg: _Optional[_Iterable[int]] = ...) -> None: ...

class RuleEvaluation(_message.Message):
    __slots__ = ("rule", "actualStringValue", "actualLongValue", "actualBoolValue", "actualDoubleValue")
    RULE_FIELD_NUMBER: _ClassVar[int]
    ACTUALSTRINGVALUE_FIELD_NUMBER: _ClassVar[int]
    ACTUALLONGVALUE_FIELD_NUMBER: _ClassVar[int]
    ACTUALBOOLVALUE_FIELD_NUMBER: _ClassVar[int]
    ACTUALDOUBLEVALUE_FIELD_NUMBER: _ClassVar[int]
    rule: Rule
    actualStringValue: _containers.RepeatedScalarFieldContainer[str]
    actualLongValue: _containers.RepeatedScalarFieldContainer[int]
    actualBoolValue: _containers.RepeatedScalarFieldContainer[bool]
    actualDoubleValue: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, rule: _Optional[_Union[Rule, _Mapping]] = ..., actualStringValue: _Optional[_Iterable[str]] = ..., actualLongValue: _Optional[_Iterable[int]] = ..., actualBoolValue: _Optional[_Iterable[bool]] = ..., actualDoubleValue: _Optional[_Iterable[float]] = ...) -> None: ...

class LibraryAppDetails(_message.Message):
    __slots__ = ("certificateHash", "refundTimeoutTimestampMsec", "postDeliveryRefundWindowMsec")
    CERTIFICATEHASH_FIELD_NUMBER: _ClassVar[int]
    REFUNDTIMEOUTTIMESTAMPMSEC_FIELD_NUMBER: _ClassVar[int]
    POSTDELIVERYREFUNDWINDOWMSEC_FIELD_NUMBER: _ClassVar[int]
    certificateHash: str
    refundTimeoutTimestampMsec: int
    postDeliveryRefundWindowMsec: int
    def __init__(self, certificateHash: _Optional[str] = ..., refundTimeoutTimestampMsec: _Optional[int] = ..., postDeliveryRefundWindowMsec: _Optional[int] = ...) -> None: ...

class LibraryInAppDetails(_message.Message):
    __slots__ = ("signedPurchaseData", "signature")
    SIGNEDPURCHASEDATA_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    signedPurchaseData: str
    signature: str
    def __init__(self, signedPurchaseData: _Optional[str] = ..., signature: _Optional[str] = ...) -> None: ...

class LibraryMutation(_message.Message):
    __slots__ = ("docid", "offerType", "documentHash", "deleted", "appDetails", "subscriptionDetails", "inAppDetails")
    DOCID_FIELD_NUMBER: _ClassVar[int]
    OFFERTYPE_FIELD_NUMBER: _ClassVar[int]
    DOCUMENTHASH_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    APPDETAILS_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTIONDETAILS_FIELD_NUMBER: _ClassVar[int]
    INAPPDETAILS_FIELD_NUMBER: _ClassVar[int]
    docid: Docid
    offerType: int
    documentHash: int
    deleted: bool
    appDetails: LibraryAppDetails
    subscriptionDetails: LibrarySubscriptionDetails
    inAppDetails: LibraryInAppDetails
    def __init__(self, docid: _Optional[_Union[Docid, _Mapping]] = ..., offerType: _Optional[int] = ..., documentHash: _Optional[int] = ..., deleted: _Optional[bool] = ..., appDetails: _Optional[_Union[LibraryAppDetails, _Mapping]] = ..., subscriptionDetails: _Optional[_Union[LibrarySubscriptionDetails, _Mapping]] = ..., inAppDetails: _Optional[_Union[LibraryInAppDetails, _Mapping]] = ...) -> None: ...

class LibrarySubscriptionDetails(_message.Message):
    __slots__ = ("initiationTimestampMsec", "validUntilTimestampMsec", "autoRenewing", "trialUntilTimestampMsec")
    INITIATIONTIMESTAMPMSEC_FIELD_NUMBER: _ClassVar[int]
    VALIDUNTILTIMESTAMPMSEC_FIELD_NUMBER: _ClassVar[int]
    AUTORENEWING_FIELD_NUMBER: _ClassVar[int]
    TRIALUNTILTIMESTAMPMSEC_FIELD_NUMBER: _ClassVar[int]
    initiationTimestampMsec: int
    validUntilTimestampMsec: int
    autoRenewing: bool
    trialUntilTimestampMsec: int
    def __init__(self, initiationTimestampMsec: _Optional[int] = ..., validUntilTimestampMsec: _Optional[int] = ..., autoRenewing: _Optional[bool] = ..., trialUntilTimestampMsec: _Optional[int] = ...) -> None: ...

class LibraryUpdate(_message.Message):
    __slots__ = ("status", "corpus", "serverToken", "mutation", "hasMore", "libraryId")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CORPUS_FIELD_NUMBER: _ClassVar[int]
    SERVERTOKEN_FIELD_NUMBER: _ClassVar[int]
    MUTATION_FIELD_NUMBER: _ClassVar[int]
    HASMORE_FIELD_NUMBER: _ClassVar[int]
    LIBRARYID_FIELD_NUMBER: _ClassVar[int]
    status: int
    corpus: int
    serverToken: bytes
    mutation: _containers.RepeatedCompositeFieldContainer[LibraryMutation]
    hasMore: bool
    libraryId: str
    def __init__(self, status: _Optional[int] = ..., corpus: _Optional[int] = ..., serverToken: _Optional[bytes] = ..., mutation: _Optional[_Iterable[_Union[LibraryMutation, _Mapping]]] = ..., hasMore: _Optional[bool] = ..., libraryId: _Optional[str] = ...) -> None: ...

class AndroidAppNotificationData(_message.Message):
    __slots__ = ("versionCode", "assetId")
    VERSIONCODE_FIELD_NUMBER: _ClassVar[int]
    ASSETID_FIELD_NUMBER: _ClassVar[int]
    versionCode: int
    assetId: str
    def __init__(self, versionCode: _Optional[int] = ..., assetId: _Optional[str] = ...) -> None: ...

class InAppNotificationData(_message.Message):
    __slots__ = ("checkoutOrderId", "inAppNotificationId")
    CHECKOUTORDERID_FIELD_NUMBER: _ClassVar[int]
    INAPPNOTIFICATIONID_FIELD_NUMBER: _ClassVar[int]
    checkoutOrderId: str
    inAppNotificationId: str
    def __init__(self, checkoutOrderId: _Optional[str] = ..., inAppNotificationId: _Optional[str] = ...) -> None: ...

class LibraryDirtyData(_message.Message):
    __slots__ = ("backend",)
    BACKEND_FIELD_NUMBER: _ClassVar[int]
    backend: int
    def __init__(self, backend: _Optional[int] = ...) -> None: ...

class Notification(_message.Message):
    __slots__ = ("notificationType", "timestamp", "docid", "docTitle", "userEmail", "appData", "appDeliveryData", "purchaseRemovalData", "userNotificationData", "inAppNotificationData", "purchaseDeclinedData", "notificationId", "libraryUpdate", "libraryDirtyData")
    NOTIFICATIONTYPE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    DOCID_FIELD_NUMBER: _ClassVar[int]
    DOCTITLE_FIELD_NUMBER: _ClassVar[int]
    USEREMAIL_FIELD_NUMBER: _ClassVar[int]
    APPDATA_FIELD_NUMBER: _ClassVar[int]
    APPDELIVERYDATA_FIELD_NUMBER: _ClassVar[int]
    PURCHASEREMOVALDATA_FIELD_NUMBER: _ClassVar[int]
    USERNOTIFICATIONDATA_FIELD_NUMBER: _ClassVar[int]
    INAPPNOTIFICATIONDATA_FIELD_NUMBER: _ClassVar[int]
    PURCHASEDECLINEDDATA_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATIONID_FIELD_NUMBER: _ClassVar[int]
    LIBRARYUPDATE_FIELD_NUMBER: _ClassVar[int]
    LIBRARYDIRTYDATA_FIELD_NUMBER: _ClassVar[int]
    notificationType: int
    timestamp: int
    docid: Docid
    docTitle: str
    userEmail: str
    appData: AndroidAppNotificationData
    appDeliveryData: AndroidAppDeliveryData
    purchaseRemovalData: PurchaseRemovalData
    userNotificationData: UserNotificationData
    inAppNotificationData: InAppNotificationData
    purchaseDeclinedData: PurchaseDeclinedData
    notificationId: str
    libraryUpdate: LibraryUpdate
    libraryDirtyData: LibraryDirtyData
    def __init__(self, notificationType: _Optional[int] = ..., timestamp: _Optional[int] = ..., docid: _Optional[_Union[Docid, _Mapping]] = ..., docTitle: _Optional[str] = ..., userEmail: _Optional[str] = ..., appData: _Optional[_Union[AndroidAppNotificationData, _Mapping]] = ..., appDeliveryData: _Optional[_Union[AndroidAppDeliveryData, _Mapping]] = ..., purchaseRemovalData: _Optional[_Union[PurchaseRemovalData, _Mapping]] = ..., userNotificationData: _Optional[_Union[UserNotificationData, _Mapping]] = ..., inAppNotificationData: _Optional[_Union[InAppNotificationData, _Mapping]] = ..., purchaseDeclinedData: _Optional[_Union[PurchaseDeclinedData, _Mapping]] = ..., notificationId: _Optional[str] = ..., libraryUpdate: _Optional[_Union[LibraryUpdate, _Mapping]] = ..., libraryDirtyData: _Optional[_Union[LibraryDirtyData, _Mapping]] = ...) -> None: ...

class PurchaseDeclinedData(_message.Message):
    __slots__ = ("reason", "showNotification")
    REASON_FIELD_NUMBER: _ClassVar[int]
    SHOWNOTIFICATION_FIELD_NUMBER: _ClassVar[int]
    reason: int
    showNotification: bool
    def __init__(self, reason: _Optional[int] = ..., showNotification: _Optional[bool] = ...) -> None: ...

class PurchaseRemovalData(_message.Message):
    __slots__ = ("malicious",)
    MALICIOUS_FIELD_NUMBER: _ClassVar[int]
    malicious: bool
    def __init__(self, malicious: _Optional[bool] = ...) -> None: ...

class UserNotificationData(_message.Message):
    __slots__ = ("notificationTitle", "notificationText", "tickerText", "dialogTitle", "dialogText")
    NOTIFICATIONTITLE_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATIONTEXT_FIELD_NUMBER: _ClassVar[int]
    TICKERTEXT_FIELD_NUMBER: _ClassVar[int]
    DIALOGTITLE_FIELD_NUMBER: _ClassVar[int]
    DIALOGTEXT_FIELD_NUMBER: _ClassVar[int]
    notificationTitle: str
    notificationText: str
    tickerText: str
    dialogTitle: str
    dialogText: str
    def __init__(self, notificationTitle: _Optional[str] = ..., notificationText: _Optional[str] = ..., tickerText: _Optional[str] = ..., dialogTitle: _Optional[str] = ..., dialogText: _Optional[str] = ...) -> None: ...

class AggregateRating(_message.Message):
    __slots__ = ("type", "starRating", "ratingsCount", "oneStarRatings", "twoStarRatings", "threeStarRatings", "fourStarRatings", "fiveStarRatings", "thumbsUpCount", "thumbsDownCount", "commentCount", "bayesianMeanRating")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    STARRATING_FIELD_NUMBER: _ClassVar[int]
    RATINGSCOUNT_FIELD_NUMBER: _ClassVar[int]
    ONESTARRATINGS_FIELD_NUMBER: _ClassVar[int]
    TWOSTARRATINGS_FIELD_NUMBER: _ClassVar[int]
    THREESTARRATINGS_FIELD_NUMBER: _ClassVar[int]
    FOURSTARRATINGS_FIELD_NUMBER: _ClassVar[int]
    FIVESTARRATINGS_FIELD_NUMBER: _ClassVar[int]
    THUMBSUPCOUNT_FIELD_NUMBER: _ClassVar[int]
    THUMBSDOWNCOUNT_FIELD_NUMBER: _ClassVar[int]
    COMMENTCOUNT_FIELD_NUMBER: _ClassVar[int]
    BAYESIANMEANRATING_FIELD_NUMBER: _ClassVar[int]
    type: int
    starRating: float
    ratingsCount: int
    oneStarRatings: int
    twoStarRatings: int
    threeStarRatings: int
    fourStarRatings: int
    fiveStarRatings: int
    thumbsUpCount: int
    thumbsDownCount: int
    commentCount: int
    bayesianMeanRating: float
    def __init__(self, type: _Optional[int] = ..., starRating: _Optional[float] = ..., ratingsCount: _Optional[int] = ..., oneStarRatings: _Optional[int] = ..., twoStarRatings: _Optional[int] = ..., threeStarRatings: _Optional[int] = ..., fourStarRatings: _Optional[int] = ..., fiveStarRatings: _Optional[int] = ..., thumbsUpCount: _Optional[int] = ..., thumbsDownCount: _Optional[int] = ..., commentCount: _Optional[int] = ..., bayesianMeanRating: _Optional[float] = ...) -> None: ...

class AcceptTosResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CarrierBillingConfig(_message.Message):
    __slots__ = ("id", "name", "apiVersion", "provisioningUrl", "credentialsUrl", "tosRequired", "perTransactionCredentialsRequired", "sendSubscriberIdWithCarrierBillingRequests")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    APIVERSION_FIELD_NUMBER: _ClassVar[int]
    PROVISIONINGURL_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALSURL_FIELD_NUMBER: _ClassVar[int]
    TOSREQUIRED_FIELD_NUMBER: _ClassVar[int]
    PERTRANSACTIONCREDENTIALSREQUIRED_FIELD_NUMBER: _ClassVar[int]
    SENDSUBSCRIBERIDWITHCARRIERBILLINGREQUESTS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    apiVersion: int
    provisioningUrl: str
    credentialsUrl: str
    tosRequired: bool
    perTransactionCredentialsRequired: bool
    sendSubscriberIdWithCarrierBillingRequests: bool
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., apiVersion: _Optional[int] = ..., provisioningUrl: _Optional[str] = ..., credentialsUrl: _Optional[str] = ..., tosRequired: _Optional[bool] = ..., perTransactionCredentialsRequired: _Optional[bool] = ..., sendSubscriberIdWithCarrierBillingRequests: _Optional[bool] = ...) -> None: ...

class BillingConfig(_message.Message):
    __slots__ = ("carrierBillingConfig", "maxIabApiVersion")
    CARRIERBILLINGCONFIG_FIELD_NUMBER: _ClassVar[int]
    MAXIABAPIVERSION_FIELD_NUMBER: _ClassVar[int]
    carrierBillingConfig: CarrierBillingConfig
    maxIabApiVersion: int
    def __init__(self, carrierBillingConfig: _Optional[_Union[CarrierBillingConfig, _Mapping]] = ..., maxIabApiVersion: _Optional[int] = ...) -> None: ...

class CorpusMetadata(_message.Message):
    __slots__ = ("backend", "name", "landingUrl", "libraryName", "recsWidgetUrl", "shopName")
    BACKEND_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LANDINGURL_FIELD_NUMBER: _ClassVar[int]
    LIBRARYNAME_FIELD_NUMBER: _ClassVar[int]
    RECSWIDGETURL_FIELD_NUMBER: _ClassVar[int]
    SHOPNAME_FIELD_NUMBER: _ClassVar[int]
    backend: int
    name: str
    landingUrl: str
    libraryName: str
    recsWidgetUrl: str
    shopName: str
    def __init__(self, backend: _Optional[int] = ..., name: _Optional[str] = ..., landingUrl: _Optional[str] = ..., libraryName: _Optional[str] = ..., recsWidgetUrl: _Optional[str] = ..., shopName: _Optional[str] = ...) -> None: ...

class Experiments(_message.Message):
    __slots__ = ("experimentId",)
    EXPERIMENTID_FIELD_NUMBER: _ClassVar[int]
    experimentId: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, experimentId: _Optional[_Iterable[str]] = ...) -> None: ...

class SelfUpdateConfig(_message.Message):
    __slots__ = ("latestClientVersionCode",)
    LATESTCLIENTVERSIONCODE_FIELD_NUMBER: _ClassVar[int]
    latestClientVersionCode: int
    def __init__(self, latestClientVersionCode: _Optional[int] = ...) -> None: ...

class TocResponse(_message.Message):
    __slots__ = ("corpus", "tosVersionDeprecated", "tosContent", "homeUrl", "experiments", "tosCheckboxTextMarketingEmails", "tosToken", "iconOverrideUrl", "selfUpdateConfig", "requiresUploadDeviceConfig", "billingConfig", "recsWidgetUrl", "socialHomeUrl", "ageVerificationRequired", "gplusSignupEnabled", "redeemEnabled", "helpUrl", "themeId", "entertainmentHomeUrl", "cookie")
    CORPUS_FIELD_NUMBER: _ClassVar[int]
    TOSVERSIONDEPRECATED_FIELD_NUMBER: _ClassVar[int]
    TOSCONTENT_FIELD_NUMBER: _ClassVar[int]
    HOMEURL_FIELD_NUMBER: _ClassVar[int]
    EXPERIMENTS_FIELD_NUMBER: _ClassVar[int]
    TOSCHECKBOXTEXTMARKETINGEMAILS_FIELD_NUMBER: _ClassVar[int]
    TOSTOKEN_FIELD_NUMBER: _ClassVar[int]
    ICONOVERRIDEURL_FIELD_NUMBER: _ClassVar[int]
    SELFUPDATECONFIG_FIELD_NUMBER: _ClassVar[int]
    REQUIRESUPLOADDEVICECONFIG_FIELD_NUMBER: _ClassVar[int]
    BILLINGCONFIG_FIELD_NUMBER: _ClassVar[int]
    RECSWIDGETURL_FIELD_NUMBER: _ClassVar[int]
    SOCIALHOMEURL_FIELD_NUMBER: _ClassVar[int]
    AGEVERIFICATIONREQUIRED_FIELD_NUMBER: _ClassVar[int]
    GPLUSSIGNUPENABLED_FIELD_NUMBER: _ClassVar[int]
    REDEEMENABLED_FIELD_NUMBER: _ClassVar[int]
    HELPURL_FIELD_NUMBER: _ClassVar[int]
    THEMEID_FIELD_NUMBER: _ClassVar[int]
    ENTERTAINMENTHOMEURL_FIELD_NUMBER: _ClassVar[int]
    COOKIE_FIELD_NUMBER: _ClassVar[int]
    corpus: _containers.RepeatedCompositeFieldContainer[CorpusMetadata]
    tosVersionDeprecated: int
    tosContent: str
    homeUrl: str
    experiments: Experiments
    tosCheckboxTextMarketingEmails: str
    tosToken: str
    iconOverrideUrl: str
    selfUpdateConfig: SelfUpdateConfig
    requiresUploadDeviceConfig: bool
    billingConfig: BillingConfig
    recsWidgetUrl: str
    socialHomeUrl: str
    ageVerificationRequired: bool
    gplusSignupEnabled: bool
    redeemEnabled: bool
    helpUrl: str
    themeId: int
    entertainmentHomeUrl: str
    cookie: str
    def __init__(self, corpus: _Optional[_Iterable[_Union[CorpusMetadata, _Mapping]]] = ..., tosVersionDeprecated: _Optional[int] = ..., tosContent: _Optional[str] = ..., homeUrl: _Optional[str] = ..., experiments: _Optional[_Union[Experiments, _Mapping]] = ..., tosCheckboxTextMarketingEmails: _Optional[str] = ..., tosToken: _Optional[str] = ..., iconOverrideUrl: _Optional[str] = ..., selfUpdateConfig: _Optional[_Union[SelfUpdateConfig, _Mapping]] = ..., requiresUploadDeviceConfig: _Optional[bool] = ..., billingConfig: _Optional[_Union[BillingConfig, _Mapping]] = ..., recsWidgetUrl: _Optional[str] = ..., socialHomeUrl: _Optional[str] = ..., ageVerificationRequired: _Optional[bool] = ..., gplusSignupEnabled: _Optional[bool] = ..., redeemEnabled: _Optional[bool] = ..., helpUrl: _Optional[str] = ..., themeId: _Optional[int] = ..., entertainmentHomeUrl: _Optional[str] = ..., cookie: _Optional[str] = ...) -> None: ...

class Payload(_message.Message):
    __slots__ = ("listResponse", "detailsResponse", "reviewResponse", "buyResponse", "searchResponse", "tocResponse", "browseResponse", "purchaseStatusResponse", "logResponse", "flagContentResponse", "bulkDetailsResponse", "deliveryResponse", "acceptTosResponse", "androidCheckinResponse", "uploadDeviceConfigResponse", "searchSuggestResponse", "testingProgramResponse")
    LISTRESPONSE_FIELD_NUMBER: _ClassVar[int]
    DETAILSRESPONSE_FIELD_NUMBER: _ClassVar[int]
    REVIEWRESPONSE_FIELD_NUMBER: _ClassVar[int]
    BUYRESPONSE_FIELD_NUMBER: _ClassVar[int]
    SEARCHRESPONSE_FIELD_NUMBER: _ClassVar[int]
    TOCRESPONSE_FIELD_NUMBER: _ClassVar[int]
    BROWSERESPONSE_FIELD_NUMBER: _ClassVar[int]
    PURCHASESTATUSRESPONSE_FIELD_NUMBER: _ClassVar[int]
    LOGRESPONSE_FIELD_NUMBER: _ClassVar[int]
    FLAGCONTENTRESPONSE_FIELD_NUMBER: _ClassVar[int]
    BULKDETAILSRESPONSE_FIELD_NUMBER: _ClassVar[int]
    DELIVERYRESPONSE_FIELD_NUMBER: _ClassVar[int]
    ACCEPTTOSRESPONSE_FIELD_NUMBER: _ClassVar[int]
    ANDROIDCHECKINRESPONSE_FIELD_NUMBER: _ClassVar[int]
    UPLOADDEVICECONFIGRESPONSE_FIELD_NUMBER: _ClassVar[int]
    SEARCHSUGGESTRESPONSE_FIELD_NUMBER: _ClassVar[int]
    TESTINGPROGRAMRESPONSE_FIELD_NUMBER: _ClassVar[int]
    listResponse: ListResponse
    detailsResponse: DetailsResponse
    reviewResponse: ReviewResponse
    buyResponse: BuyResponse
    searchResponse: SearchResponse
    tocResponse: TocResponse
    browseResponse: BrowseResponse
    purchaseStatusResponse: PurchaseStatusResponse
    logResponse: str
    flagContentResponse: str
    bulkDetailsResponse: BulkDetailsResponse
    deliveryResponse: DeliveryResponse
    acceptTosResponse: AcceptTosResponse
    androidCheckinResponse: AndroidCheckinResponse
    uploadDeviceConfigResponse: UploadDeviceConfigResponse
    searchSuggestResponse: SearchSuggestResponse
    testingProgramResponse: TestingProgramResponse
    def __init__(self, listResponse: _Optional[_Union[ListResponse, _Mapping]] = ..., detailsResponse: _Optional[_Union[DetailsResponse, _Mapping]] = ..., reviewResponse: _Optional[_Union[ReviewResponse, _Mapping]] = ..., buyResponse: _Optional[_Union[BuyResponse, _Mapping]] = ..., searchResponse: _Optional[_Union[SearchResponse, _Mapping]] = ..., tocResponse: _Optional[_Union[TocResponse, _Mapping]] = ..., browseResponse: _Optional[_Union[BrowseResponse, _Mapping]] = ..., purchaseStatusResponse: _Optional[_Union[PurchaseStatusResponse, _Mapping]] = ..., logResponse: _Optional[str] = ..., flagContentResponse: _Optional[str] = ..., bulkDetailsResponse: _Optional[_Union[BulkDetailsResponse, _Mapping]] = ..., deliveryResponse: _Optional[_Union[DeliveryResponse, _Mapping]] = ..., acceptTosResponse: _Optional[_Union[AcceptTosResponse, _Mapping]] = ..., androidCheckinResponse: _Optional[_Union[AndroidCheckinResponse, _Mapping]] = ..., uploadDeviceConfigResponse: _Optional[_Union[UploadDeviceConfigResponse, _Mapping]] = ..., searchSuggestResponse: _Optional[_Union[SearchSuggestResponse, _Mapping]] = ..., testingProgramResponse: _Optional[_Union[TestingProgramResponse, _Mapping]] = ...) -> None: ...

class PreFetch(_message.Message):
    __slots__ = ("url", "response", "etag", "ttl", "softTtl")
    URL_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    TTL_FIELD_NUMBER: _ClassVar[int]
    SOFTTTL_FIELD_NUMBER: _ClassVar[int]
    url: str
    response: ResponseWrapper
    etag: str
    ttl: int
    softTtl: int
    def __init__(self, url: _Optional[str] = ..., response: _Optional[_Union[ResponseWrapper, _Mapping]] = ..., etag: _Optional[str] = ..., ttl: _Optional[int] = ..., softTtl: _Optional[int] = ...) -> None: ...

class ServerMetadata(_message.Message):
    __slots__ = ("latencyMillis",)
    LATENCYMILLIS_FIELD_NUMBER: _ClassVar[int]
    latencyMillis: int
    def __init__(self, latencyMillis: _Optional[int] = ...) -> None: ...

class Targets(_message.Message):
    __slots__ = ("targetId", "signature")
    TARGETID_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    targetId: _containers.RepeatedScalarFieldContainer[int]
    signature: bytes
    def __init__(self, targetId: _Optional[_Iterable[int]] = ..., signature: _Optional[bytes] = ...) -> None: ...

class ServerCookie(_message.Message):
    __slots__ = ("type", "token")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    type: int
    token: bytes
    def __init__(self, type: _Optional[int] = ..., token: _Optional[bytes] = ...) -> None: ...

class ServerCookies(_message.Message):
    __slots__ = ("serverCookie",)
    SERVERCOOKIE_FIELD_NUMBER: _ClassVar[int]
    serverCookie: _containers.RepeatedCompositeFieldContainer[ServerCookie]
    def __init__(self, serverCookie: _Optional[_Iterable[_Union[ServerCookie, _Mapping]]] = ...) -> None: ...

class ResponseWrapper(_message.Message):
    __slots__ = ("payload", "commands", "preFetch", "notification", "serverMetadata", "targets", "serverCookies", "serverLogsCookie")
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    COMMANDS_FIELD_NUMBER: _ClassVar[int]
    PREFETCH_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_FIELD_NUMBER: _ClassVar[int]
    SERVERMETADATA_FIELD_NUMBER: _ClassVar[int]
    TARGETS_FIELD_NUMBER: _ClassVar[int]
    SERVERCOOKIES_FIELD_NUMBER: _ClassVar[int]
    SERVERLOGSCOOKIE_FIELD_NUMBER: _ClassVar[int]
    payload: Payload
    commands: ServerCommands
    preFetch: _containers.RepeatedCompositeFieldContainer[PreFetch]
    notification: _containers.RepeatedCompositeFieldContainer[Notification]
    serverMetadata: ServerMetadata
    targets: Targets
    serverCookies: ServerCookies
    serverLogsCookie: bytes
    def __init__(self, payload: _Optional[_Union[Payload, _Mapping]] = ..., commands: _Optional[_Union[ServerCommands, _Mapping]] = ..., preFetch: _Optional[_Iterable[_Union[PreFetch, _Mapping]]] = ..., notification: _Optional[_Iterable[_Union[Notification, _Mapping]]] = ..., serverMetadata: _Optional[_Union[ServerMetadata, _Mapping]] = ..., targets: _Optional[_Union[Targets, _Mapping]] = ..., serverCookies: _Optional[_Union[ServerCookies, _Mapping]] = ..., serverLogsCookie: _Optional[bytes] = ...) -> None: ...

class ResponseWrapperApi(_message.Message):
    __slots__ = ("payload",)
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: PayloadApi
    def __init__(self, payload: _Optional[_Union[PayloadApi, _Mapping]] = ...) -> None: ...

class PayloadApi(_message.Message):
    __slots__ = ("userProfileResponse",)
    USERPROFILERESPONSE_FIELD_NUMBER: _ClassVar[int]
    userProfileResponse: UserProfileResponse
    def __init__(self, userProfileResponse: _Optional[_Union[UserProfileResponse, _Mapping]] = ...) -> None: ...

class UserProfileResponse(_message.Message):
    __slots__ = ("userProfile",)
    USERPROFILE_FIELD_NUMBER: _ClassVar[int]
    userProfile: UserProfile
    def __init__(self, userProfile: _Optional[_Union[UserProfile, _Mapping]] = ...) -> None: ...

class ServerCommands(_message.Message):
    __slots__ = ("clearCache", "displayErrorMessage", "logErrorStacktrace")
    CLEARCACHE_FIELD_NUMBER: _ClassVar[int]
    DISPLAYERRORMESSAGE_FIELD_NUMBER: _ClassVar[int]
    LOGERRORSTACKTRACE_FIELD_NUMBER: _ClassVar[int]
    clearCache: bool
    displayErrorMessage: str
    logErrorStacktrace: str
    def __init__(self, clearCache: _Optional[bool] = ..., displayErrorMessage: _Optional[str] = ..., logErrorStacktrace: _Optional[str] = ...) -> None: ...

class GetReviewsResponse(_message.Message):
    __slots__ = ("review", "matchingCount")
    REVIEW_FIELD_NUMBER: _ClassVar[int]
    MATCHINGCOUNT_FIELD_NUMBER: _ClassVar[int]
    review: _containers.RepeatedCompositeFieldContainer[Review]
    matchingCount: int
    def __init__(self, review: _Optional[_Iterable[_Union[Review, _Mapping]]] = ..., matchingCount: _Optional[int] = ...) -> None: ...

class Review(_message.Message):
    __slots__ = ("authorName", "url", "source", "documentVersion", "timestampMsec", "starRating", "title", "comment", "commentId", "deviceName", "replyText", "replyTimestampMsec", "author", "userProfile")
    AUTHORNAME_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    DOCUMENTVERSION_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMPMSEC_FIELD_NUMBER: _ClassVar[int]
    STARRATING_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    COMMENTID_FIELD_NUMBER: _ClassVar[int]
    DEVICENAME_FIELD_NUMBER: _ClassVar[int]
    REPLYTEXT_FIELD_NUMBER: _ClassVar[int]
    REPLYTIMESTAMPMSEC_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    USERPROFILE_FIELD_NUMBER: _ClassVar[int]
    authorName: str
    url: str
    source: str
    documentVersion: str
    timestampMsec: int
    starRating: int
    title: str
    comment: str
    commentId: str
    deviceName: str
    replyText: str
    replyTimestampMsec: int
    author: ReviewAuthor
    userProfile: UserProfile
    def __init__(self, authorName: _Optional[str] = ..., url: _Optional[str] = ..., source: _Optional[str] = ..., documentVersion: _Optional[str] = ..., timestampMsec: _Optional[int] = ..., starRating: _Optional[int] = ..., title: _Optional[str] = ..., comment: _Optional[str] = ..., commentId: _Optional[str] = ..., deviceName: _Optional[str] = ..., replyText: _Optional[str] = ..., replyTimestampMsec: _Optional[int] = ..., author: _Optional[_Union[ReviewAuthor, _Mapping]] = ..., userProfile: _Optional[_Union[UserProfile, _Mapping]] = ...) -> None: ...

class ReviewAuthor(_message.Message):
    __slots__ = ("name", "avatar")
    NAME_FIELD_NUMBER: _ClassVar[int]
    AVATAR_FIELD_NUMBER: _ClassVar[int]
    name: str
    avatar: Image
    def __init__(self, name: _Optional[str] = ..., avatar: _Optional[_Union[Image, _Mapping]] = ...) -> None: ...

class UserProfile(_message.Message):
    __slots__ = ("personIdString", "personId", "unknown1", "unknown2", "name", "image", "googlePlusUrl", "googlePlusTagline")
    PERSONIDSTRING_FIELD_NUMBER: _ClassVar[int]
    PERSONID_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN1_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN2_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    GOOGLEPLUSURL_FIELD_NUMBER: _ClassVar[int]
    GOOGLEPLUSTAGLINE_FIELD_NUMBER: _ClassVar[int]
    personIdString: str
    personId: str
    unknown1: int
    unknown2: int
    name: str
    image: _containers.RepeatedCompositeFieldContainer[Image]
    googlePlusUrl: str
    googlePlusTagline: str
    def __init__(self, personIdString: _Optional[str] = ..., personId: _Optional[str] = ..., unknown1: _Optional[int] = ..., unknown2: _Optional[int] = ..., name: _Optional[str] = ..., image: _Optional[_Iterable[_Union[Image, _Mapping]]] = ..., googlePlusUrl: _Optional[str] = ..., googlePlusTagline: _Optional[str] = ...) -> None: ...

class ReviewResponse(_message.Message):
    __slots__ = ("getResponse", "nextPageUrl", "userReview")
    GETRESPONSE_FIELD_NUMBER: _ClassVar[int]
    NEXTPAGEURL_FIELD_NUMBER: _ClassVar[int]
    USERREVIEW_FIELD_NUMBER: _ClassVar[int]
    getResponse: GetReviewsResponse
    nextPageUrl: str
    userReview: Review
    def __init__(self, getResponse: _Optional[_Union[GetReviewsResponse, _Mapping]] = ..., nextPageUrl: _Optional[str] = ..., userReview: _Optional[_Union[Review, _Mapping]] = ...) -> None: ...

class RelatedSearch(_message.Message):
    __slots__ = ("searchUrl", "header", "backendId", "docType", "current")
    SEARCHURL_FIELD_NUMBER: _ClassVar[int]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    BACKENDID_FIELD_NUMBER: _ClassVar[int]
    DOCTYPE_FIELD_NUMBER: _ClassVar[int]
    CURRENT_FIELD_NUMBER: _ClassVar[int]
    searchUrl: str
    header: str
    backendId: int
    docType: int
    current: bool
    def __init__(self, searchUrl: _Optional[str] = ..., header: _Optional[str] = ..., backendId: _Optional[int] = ..., docType: _Optional[int] = ..., current: _Optional[bool] = ...) -> None: ...

class SearchResponse(_message.Message):
    __slots__ = ("originalQuery", "suggestedQuery", "aggregateQuery", "bucket", "doc", "relatedSearch", "nextPageUrl")
    ORIGINALQUERY_FIELD_NUMBER: _ClassVar[int]
    SUGGESTEDQUERY_FIELD_NUMBER: _ClassVar[int]
    AGGREGATEQUERY_FIELD_NUMBER: _ClassVar[int]
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    DOC_FIELD_NUMBER: _ClassVar[int]
    RELATEDSEARCH_FIELD_NUMBER: _ClassVar[int]
    NEXTPAGEURL_FIELD_NUMBER: _ClassVar[int]
    originalQuery: str
    suggestedQuery: str
    aggregateQuery: bool
    bucket: _containers.RepeatedCompositeFieldContainer[Bucket]
    doc: _containers.RepeatedCompositeFieldContainer[DocV2]
    relatedSearch: _containers.RepeatedCompositeFieldContainer[RelatedSearch]
    nextPageUrl: str
    def __init__(self, originalQuery: _Optional[str] = ..., suggestedQuery: _Optional[str] = ..., aggregateQuery: _Optional[bool] = ..., bucket: _Optional[_Iterable[_Union[Bucket, _Mapping]]] = ..., doc: _Optional[_Iterable[_Union[DocV2, _Mapping]]] = ..., relatedSearch: _Optional[_Iterable[_Union[RelatedSearch, _Mapping]]] = ..., nextPageUrl: _Optional[str] = ...) -> None: ...

class SearchSuggestResponse(_message.Message):
    __slots__ = ("entry",)
    ENTRY_FIELD_NUMBER: _ClassVar[int]
    entry: _containers.RepeatedCompositeFieldContainer[SearchSuggestEntry]
    def __init__(self, entry: _Optional[_Iterable[_Union[SearchSuggestEntry, _Mapping]]] = ...) -> None: ...

class SearchSuggestEntry(_message.Message):
    __slots__ = ("type", "suggestedQuery", "imageContainer", "title", "packageNameContainer")
    class ImageContainer(_message.Message):
        __slots__ = ("imageUrl",)
        IMAGEURL_FIELD_NUMBER: _ClassVar[int]
        imageUrl: str
        def __init__(self, imageUrl: _Optional[str] = ...) -> None: ...
    class PackageNameContainer(_message.Message):
        __slots__ = ("packageName",)
        PACKAGENAME_FIELD_NUMBER: _ClassVar[int]
        packageName: str
        def __init__(self, packageName: _Optional[str] = ...) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SUGGESTEDQUERY_FIELD_NUMBER: _ClassVar[int]
    IMAGECONTAINER_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    PACKAGENAMECONTAINER_FIELD_NUMBER: _ClassVar[int]
    type: int
    suggestedQuery: str
    imageContainer: SearchSuggestEntry.ImageContainer
    title: str
    packageNameContainer: SearchSuggestEntry.PackageNameContainer
    def __init__(self, type: _Optional[int] = ..., suggestedQuery: _Optional[str] = ..., imageContainer: _Optional[_Union[SearchSuggestEntry.ImageContainer, _Mapping]] = ..., title: _Optional[str] = ..., packageNameContainer: _Optional[_Union[SearchSuggestEntry.PackageNameContainer, _Mapping]] = ...) -> None: ...

class TestingProgramResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: TestingProgramResult
    def __init__(self, result: _Optional[_Union[TestingProgramResult, _Mapping]] = ...) -> None: ...

class TestingProgramResult(_message.Message):
    __slots__ = ("details",)
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    details: TestingProgramDetails
    def __init__(self, details: _Optional[_Union[TestingProgramDetails, _Mapping]] = ...) -> None: ...

class TestingProgramDetails(_message.Message):
    __slots__ = ("flag1", "id", "unsubscribed")
    FLAG1_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    UNSUBSCRIBED_FIELD_NUMBER: _ClassVar[int]
    flag1: bool
    id: int
    unsubscribed: bool
    def __init__(self, flag1: _Optional[bool] = ..., id: _Optional[int] = ..., unsubscribed: _Optional[bool] = ...) -> None: ...

class LogRequest(_message.Message):
    __slots__ = ("timestamp", "downloadConfirmationQuery")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    DOWNLOADCONFIRMATIONQUERY_FIELD_NUMBER: _ClassVar[int]
    timestamp: int
    downloadConfirmationQuery: str
    def __init__(self, timestamp: _Optional[int] = ..., downloadConfirmationQuery: _Optional[str] = ...) -> None: ...

class TestingProgramRequest(_message.Message):
    __slots__ = ("packageName", "subscribe")
    PACKAGENAME_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIBE_FIELD_NUMBER: _ClassVar[int]
    packageName: str
    subscribe: bool
    def __init__(self, packageName: _Optional[str] = ..., subscribe: _Optional[bool] = ...) -> None: ...

class UploadDeviceConfigRequest(_message.Message):
    __slots__ = ("deviceConfiguration", "manufacturer", "gcmRegistrationId")
    DEVICECONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    MANUFACTURER_FIELD_NUMBER: _ClassVar[int]
    GCMREGISTRATIONID_FIELD_NUMBER: _ClassVar[int]
    deviceConfiguration: DeviceConfigurationProto
    manufacturer: str
    gcmRegistrationId: str
    def __init__(self, deviceConfiguration: _Optional[_Union[DeviceConfigurationProto, _Mapping]] = ..., manufacturer: _Optional[str] = ..., gcmRegistrationId: _Optional[str] = ...) -> None: ...

class UploadDeviceConfigResponse(_message.Message):
    __slots__ = ("uploadDeviceConfigToken",)
    UPLOADDEVICECONFIGTOKEN_FIELD_NUMBER: _ClassVar[int]
    uploadDeviceConfigToken: str
    def __init__(self, uploadDeviceConfigToken: _Optional[str] = ...) -> None: ...

class AndroidCheckinRequest(_message.Message):
    __slots__ = ("imei", "id", "digest", "checkin", "desiredBuild", "locale", "loggingId", "marketCheckin", "macAddr", "meid", "accountCookie", "timeZone", "securityToken", "version", "otaCert", "serialNumber", "esn", "deviceConfiguration", "macAddrType", "fragment", "userName", "userSerialNumber")
    IMEI_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    DIGEST_FIELD_NUMBER: _ClassVar[int]
    CHECKIN_FIELD_NUMBER: _ClassVar[int]
    DESIREDBUILD_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    LOGGINGID_FIELD_NUMBER: _ClassVar[int]
    MARKETCHECKIN_FIELD_NUMBER: _ClassVar[int]
    MACADDR_FIELD_NUMBER: _ClassVar[int]
    MEID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTCOOKIE_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    SECURITYTOKEN_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    OTACERT_FIELD_NUMBER: _ClassVar[int]
    SERIALNUMBER_FIELD_NUMBER: _ClassVar[int]
    ESN_FIELD_NUMBER: _ClassVar[int]
    DEVICECONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    MACADDRTYPE_FIELD_NUMBER: _ClassVar[int]
    FRAGMENT_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    USERSERIALNUMBER_FIELD_NUMBER: _ClassVar[int]
    imei: str
    id: int
    digest: str
    checkin: AndroidCheckinProto
    desiredBuild: str
    locale: str
    loggingId: int
    marketCheckin: str
    macAddr: _containers.RepeatedScalarFieldContainer[str]
    meid: str
    accountCookie: _containers.RepeatedScalarFieldContainer[str]
    timeZone: str
    securityToken: int
    version: int
    otaCert: _containers.RepeatedScalarFieldContainer[str]
    serialNumber: str
    esn: str
    deviceConfiguration: DeviceConfigurationProto
    macAddrType: _containers.RepeatedScalarFieldContainer[str]
    fragment: int
    userName: str
    userSerialNumber: int
    def __init__(self, imei: _Optional[str] = ..., id: _Optional[int] = ..., digest: _Optional[str] = ..., checkin: _Optional[_Union[AndroidCheckinProto, _Mapping]] = ..., desiredBuild: _Optional[str] = ..., locale: _Optional[str] = ..., loggingId: _Optional[int] = ..., marketCheckin: _Optional[str] = ..., macAddr: _Optional[_Iterable[str]] = ..., meid: _Optional[str] = ..., accountCookie: _Optional[_Iterable[str]] = ..., timeZone: _Optional[str] = ..., securityToken: _Optional[int] = ..., version: _Optional[int] = ..., otaCert: _Optional[_Iterable[str]] = ..., serialNumber: _Optional[str] = ..., esn: _Optional[str] = ..., deviceConfiguration: _Optional[_Union[DeviceConfigurationProto, _Mapping]] = ..., macAddrType: _Optional[_Iterable[str]] = ..., fragment: _Optional[int] = ..., userName: _Optional[str] = ..., userSerialNumber: _Optional[int] = ...) -> None: ...

class AndroidCheckinResponse(_message.Message):
    __slots__ = ("statsOk", "intent", "timeMsec", "digest", "setting", "marketOk", "androidId", "securityToken", "settingsDiff", "deleteSetting", "deviceCheckinConsistencyToken")
    STATSOK_FIELD_NUMBER: _ClassVar[int]
    INTENT_FIELD_NUMBER: _ClassVar[int]
    TIMEMSEC_FIELD_NUMBER: _ClassVar[int]
    DIGEST_FIELD_NUMBER: _ClassVar[int]
    SETTING_FIELD_NUMBER: _ClassVar[int]
    MARKETOK_FIELD_NUMBER: _ClassVar[int]
    ANDROIDID_FIELD_NUMBER: _ClassVar[int]
    SECURITYTOKEN_FIELD_NUMBER: _ClassVar[int]
    SETTINGSDIFF_FIELD_NUMBER: _ClassVar[int]
    DELETESETTING_FIELD_NUMBER: _ClassVar[int]
    DEVICECHECKINCONSISTENCYTOKEN_FIELD_NUMBER: _ClassVar[int]
    statsOk: bool
    intent: _containers.RepeatedCompositeFieldContainer[AndroidIntentProto]
    timeMsec: int
    digest: str
    setting: _containers.RepeatedCompositeFieldContainer[GservicesSetting]
    marketOk: bool
    androidId: int
    securityToken: int
    settingsDiff: bool
    deleteSetting: _containers.RepeatedScalarFieldContainer[str]
    deviceCheckinConsistencyToken: str
    def __init__(self, statsOk: _Optional[bool] = ..., intent: _Optional[_Iterable[_Union[AndroidIntentProto, _Mapping]]] = ..., timeMsec: _Optional[int] = ..., digest: _Optional[str] = ..., setting: _Optional[_Iterable[_Union[GservicesSetting, _Mapping]]] = ..., marketOk: _Optional[bool] = ..., androidId: _Optional[int] = ..., securityToken: _Optional[int] = ..., settingsDiff: _Optional[bool] = ..., deleteSetting: _Optional[_Iterable[str]] = ..., deviceCheckinConsistencyToken: _Optional[str] = ...) -> None: ...

class GservicesSetting(_message.Message):
    __slots__ = ("name", "value")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: bytes
    value: bytes
    def __init__(self, name: _Optional[bytes] = ..., value: _Optional[bytes] = ...) -> None: ...

class AndroidBuildProto(_message.Message):
    __slots__ = ("id", "product", "carrier", "radio", "bootloader", "client", "timestamp", "googleServices", "device", "sdkVersion", "model", "manufacturer", "buildProduct", "otaInstalled")
    ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_FIELD_NUMBER: _ClassVar[int]
    CARRIER_FIELD_NUMBER: _ClassVar[int]
    RADIO_FIELD_NUMBER: _ClassVar[int]
    BOOTLOADER_FIELD_NUMBER: _ClassVar[int]
    CLIENT_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    GOOGLESERVICES_FIELD_NUMBER: _ClassVar[int]
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    SDKVERSION_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    MANUFACTURER_FIELD_NUMBER: _ClassVar[int]
    BUILDPRODUCT_FIELD_NUMBER: _ClassVar[int]
    OTAINSTALLED_FIELD_NUMBER: _ClassVar[int]
    id: str
    product: str
    carrier: str
    radio: str
    bootloader: str
    client: str
    timestamp: int
    googleServices: int
    device: str
    sdkVersion: int
    model: str
    manufacturer: str
    buildProduct: str
    otaInstalled: bool
    def __init__(self, id: _Optional[str] = ..., product: _Optional[str] = ..., carrier: _Optional[str] = ..., radio: _Optional[str] = ..., bootloader: _Optional[str] = ..., client: _Optional[str] = ..., timestamp: _Optional[int] = ..., googleServices: _Optional[int] = ..., device: _Optional[str] = ..., sdkVersion: _Optional[int] = ..., model: _Optional[str] = ..., manufacturer: _Optional[str] = ..., buildProduct: _Optional[str] = ..., otaInstalled: _Optional[bool] = ...) -> None: ...

class AndroidCheckinProto(_message.Message):
    __slots__ = ("build", "lastCheckinMsec", "event", "stat", "requestedGroup", "cellOperator", "simOperator", "roaming", "userNumber")
    BUILD_FIELD_NUMBER: _ClassVar[int]
    LASTCHECKINMSEC_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    STAT_FIELD_NUMBER: _ClassVar[int]
    REQUESTEDGROUP_FIELD_NUMBER: _ClassVar[int]
    CELLOPERATOR_FIELD_NUMBER: _ClassVar[int]
    SIMOPERATOR_FIELD_NUMBER: _ClassVar[int]
    ROAMING_FIELD_NUMBER: _ClassVar[int]
    USERNUMBER_FIELD_NUMBER: _ClassVar[int]
    build: AndroidBuildProto
    lastCheckinMsec: int
    event: _containers.RepeatedCompositeFieldContainer[AndroidEventProto]
    stat: _containers.RepeatedCompositeFieldContainer[AndroidStatisticProto]
    requestedGroup: _containers.RepeatedScalarFieldContainer[str]
    cellOperator: str
    simOperator: str
    roaming: str
    userNumber: int
    def __init__(self, build: _Optional[_Union[AndroidBuildProto, _Mapping]] = ..., lastCheckinMsec: _Optional[int] = ..., event: _Optional[_Iterable[_Union[AndroidEventProto, _Mapping]]] = ..., stat: _Optional[_Iterable[_Union[AndroidStatisticProto, _Mapping]]] = ..., requestedGroup: _Optional[_Iterable[str]] = ..., cellOperator: _Optional[str] = ..., simOperator: _Optional[str] = ..., roaming: _Optional[str] = ..., userNumber: _Optional[int] = ...) -> None: ...

class AndroidEventProto(_message.Message):
    __slots__ = ("tag", "value", "timeMsec")
    TAG_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    TIMEMSEC_FIELD_NUMBER: _ClassVar[int]
    tag: str
    value: str
    timeMsec: int
    def __init__(self, tag: _Optional[str] = ..., value: _Optional[str] = ..., timeMsec: _Optional[int] = ...) -> None: ...

class AndroidIntentProto(_message.Message):
    __slots__ = ("action", "dataUri", "mimeType", "javaClass", "extra")
    class Extra(_message.Message):
        __slots__ = ("name", "value")
        NAME_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        name: str
        value: str
        def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ACTION_FIELD_NUMBER: _ClassVar[int]
    DATAURI_FIELD_NUMBER: _ClassVar[int]
    MIMETYPE_FIELD_NUMBER: _ClassVar[int]
    JAVACLASS_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    action: str
    dataUri: str
    mimeType: str
    javaClass: str
    extra: _containers.RepeatedCompositeFieldContainer[AndroidIntentProto.Extra]
    def __init__(self, action: _Optional[str] = ..., dataUri: _Optional[str] = ..., mimeType: _Optional[str] = ..., javaClass: _Optional[str] = ..., extra: _Optional[_Iterable[_Union[AndroidIntentProto.Extra, _Mapping]]] = ...) -> None: ...

class AndroidStatisticProto(_message.Message):
    __slots__ = ("tag", "count", "sum")
    TAG_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    SUM_FIELD_NUMBER: _ClassVar[int]
    tag: str
    count: int
    sum: float
    def __init__(self, tag: _Optional[str] = ..., count: _Optional[int] = ..., sum: _Optional[float] = ...) -> None: ...

class ClientLibraryState(_message.Message):
    __slots__ = ("corpus", "serverToken", "hashCodeSum", "librarySize", "libraryId")
    CORPUS_FIELD_NUMBER: _ClassVar[int]
    SERVERTOKEN_FIELD_NUMBER: _ClassVar[int]
    HASHCODESUM_FIELD_NUMBER: _ClassVar[int]
    LIBRARYSIZE_FIELD_NUMBER: _ClassVar[int]
    LIBRARYID_FIELD_NUMBER: _ClassVar[int]
    corpus: int
    serverToken: bytes
    hashCodeSum: int
    librarySize: int
    libraryId: str
    def __init__(self, corpus: _Optional[int] = ..., serverToken: _Optional[bytes] = ..., hashCodeSum: _Optional[int] = ..., librarySize: _Optional[int] = ..., libraryId: _Optional[str] = ...) -> None: ...

class AndroidDataUsageProto(_message.Message):
    __slots__ = ("version", "currentReportMsec", "keyToPackageNameMapping", "payloadLevelAppStat", "ipLayerNetworkStat")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    CURRENTREPORTMSEC_FIELD_NUMBER: _ClassVar[int]
    KEYTOPACKAGENAMEMAPPING_FIELD_NUMBER: _ClassVar[int]
    PAYLOADLEVELAPPSTAT_FIELD_NUMBER: _ClassVar[int]
    IPLAYERNETWORKSTAT_FIELD_NUMBER: _ClassVar[int]
    version: int
    currentReportMsec: int
    keyToPackageNameMapping: _containers.RepeatedCompositeFieldContainer[KeyToPackageNameMapping]
    payloadLevelAppStat: _containers.RepeatedCompositeFieldContainer[PayloadLevelAppStat]
    ipLayerNetworkStat: _containers.RepeatedCompositeFieldContainer[IpLayerNetworkStat]
    def __init__(self, version: _Optional[int] = ..., currentReportMsec: _Optional[int] = ..., keyToPackageNameMapping: _Optional[_Iterable[_Union[KeyToPackageNameMapping, _Mapping]]] = ..., payloadLevelAppStat: _Optional[_Iterable[_Union[PayloadLevelAppStat, _Mapping]]] = ..., ipLayerNetworkStat: _Optional[_Iterable[_Union[IpLayerNetworkStat, _Mapping]]] = ...) -> None: ...

class AndroidUsageStatsReport(_message.Message):
    __slots__ = ("androidId", "loggingId", "usageStats")
    ANDROIDID_FIELD_NUMBER: _ClassVar[int]
    LOGGINGID_FIELD_NUMBER: _ClassVar[int]
    USAGESTATS_FIELD_NUMBER: _ClassVar[int]
    androidId: int
    loggingId: int
    usageStats: UsageStatsExtensionProto
    def __init__(self, androidId: _Optional[int] = ..., loggingId: _Optional[int] = ..., usageStats: _Optional[_Union[UsageStatsExtensionProto, _Mapping]] = ...) -> None: ...

class AppBucket(_message.Message):
    __slots__ = ("bucketStartMsec", "bucketDurationMsec", "statCounters", "operationCount")
    BUCKETSTARTMSEC_FIELD_NUMBER: _ClassVar[int]
    BUCKETDURATIONMSEC_FIELD_NUMBER: _ClassVar[int]
    STATCOUNTERS_FIELD_NUMBER: _ClassVar[int]
    OPERATIONCOUNT_FIELD_NUMBER: _ClassVar[int]
    bucketStartMsec: int
    bucketDurationMsec: int
    statCounters: _containers.RepeatedCompositeFieldContainer[StatCounters]
    operationCount: int
    def __init__(self, bucketStartMsec: _Optional[int] = ..., bucketDurationMsec: _Optional[int] = ..., statCounters: _Optional[_Iterable[_Union[StatCounters, _Mapping]]] = ..., operationCount: _Optional[int] = ...) -> None: ...

class CounterData(_message.Message):
    __slots__ = ("bytes", "packets")
    BYTES_FIELD_NUMBER: _ClassVar[int]
    PACKETS_FIELD_NUMBER: _ClassVar[int]
    bytes: int
    packets: int
    def __init__(self, bytes: _Optional[int] = ..., packets: _Optional[int] = ...) -> None: ...

class IpLayerAppStat(_message.Message):
    __slots__ = ("packageKey", "applicationTag", "ipLayerAppBucket")
    PACKAGEKEY_FIELD_NUMBER: _ClassVar[int]
    APPLICATIONTAG_FIELD_NUMBER: _ClassVar[int]
    IPLAYERAPPBUCKET_FIELD_NUMBER: _ClassVar[int]
    packageKey: int
    applicationTag: int
    ipLayerAppBucket: _containers.RepeatedCompositeFieldContainer[AppBucket]
    def __init__(self, packageKey: _Optional[int] = ..., applicationTag: _Optional[int] = ..., ipLayerAppBucket: _Optional[_Iterable[_Union[AppBucket, _Mapping]]] = ...) -> None: ...

class IpLayerNetworkBucket(_message.Message):
    __slots__ = ("bucketStartMsec", "bucketDurationMsec", "statCounters", "networkActiveDuration")
    BUCKETSTARTMSEC_FIELD_NUMBER: _ClassVar[int]
    BUCKETDURATIONMSEC_FIELD_NUMBER: _ClassVar[int]
    STATCOUNTERS_FIELD_NUMBER: _ClassVar[int]
    NETWORKACTIVEDURATION_FIELD_NUMBER: _ClassVar[int]
    bucketStartMsec: int
    bucketDurationMsec: int
    statCounters: _containers.RepeatedCompositeFieldContainer[StatCounters]
    networkActiveDuration: int
    def __init__(self, bucketStartMsec: _Optional[int] = ..., bucketDurationMsec: _Optional[int] = ..., statCounters: _Optional[_Iterable[_Union[StatCounters, _Mapping]]] = ..., networkActiveDuration: _Optional[int] = ...) -> None: ...

class IpLayerNetworkStat(_message.Message):
    __slots__ = ("networkDetails", "type", "ipLayerNetworkBucket", "ipLayerAppStat")
    NETWORKDETAILS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    IPLAYERNETWORKBUCKET_FIELD_NUMBER: _ClassVar[int]
    IPLAYERAPPSTAT_FIELD_NUMBER: _ClassVar[int]
    networkDetails: str
    type: int
    ipLayerNetworkBucket: _containers.RepeatedCompositeFieldContainer[IpLayerNetworkBucket]
    ipLayerAppStat: _containers.RepeatedCompositeFieldContainer[IpLayerAppStat]
    def __init__(self, networkDetails: _Optional[str] = ..., type: _Optional[int] = ..., ipLayerNetworkBucket: _Optional[_Iterable[_Union[IpLayerNetworkBucket, _Mapping]]] = ..., ipLayerAppStat: _Optional[_Iterable[_Union[IpLayerAppStat, _Mapping]]] = ...) -> None: ...

class KeyToPackageNameMapping(_message.Message):
    __slots__ = ("packageKey", "uidName", "sharedPackageList")
    PACKAGEKEY_FIELD_NUMBER: _ClassVar[int]
    UIDNAME_FIELD_NUMBER: _ClassVar[int]
    SHAREDPACKAGELIST_FIELD_NUMBER: _ClassVar[int]
    packageKey: int
    uidName: str
    sharedPackageList: _containers.RepeatedCompositeFieldContainer[PackageInfo]
    def __init__(self, packageKey: _Optional[int] = ..., uidName: _Optional[str] = ..., sharedPackageList: _Optional[_Iterable[_Union[PackageInfo, _Mapping]]] = ...) -> None: ...

class PackageInfo(_message.Message):
    __slots__ = ("pkgName", "versionCode")
    PKGNAME_FIELD_NUMBER: _ClassVar[int]
    VERSIONCODE_FIELD_NUMBER: _ClassVar[int]
    pkgName: str
    versionCode: int
    def __init__(self, pkgName: _Optional[str] = ..., versionCode: _Optional[int] = ...) -> None: ...

class PayloadLevelAppStat(_message.Message):
    __slots__ = ("packageKey", "applicationTag", "payloadLevelAppBucket")
    PACKAGEKEY_FIELD_NUMBER: _ClassVar[int]
    APPLICATIONTAG_FIELD_NUMBER: _ClassVar[int]
    PAYLOADLEVELAPPBUCKET_FIELD_NUMBER: _ClassVar[int]
    packageKey: int
    applicationTag: int
    payloadLevelAppBucket: _containers.RepeatedCompositeFieldContainer[AppBucket]
    def __init__(self, packageKey: _Optional[int] = ..., applicationTag: _Optional[int] = ..., payloadLevelAppBucket: _Optional[_Iterable[_Union[AppBucket, _Mapping]]] = ...) -> None: ...

class StatCounters(_message.Message):
    __slots__ = ("networkProto", "direction", "counterData", "fgBg")
    NETWORKPROTO_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    COUNTERDATA_FIELD_NUMBER: _ClassVar[int]
    FGBG_FIELD_NUMBER: _ClassVar[int]
    networkProto: int
    direction: int
    counterData: CounterData
    fgBg: int
    def __init__(self, networkProto: _Optional[int] = ..., direction: _Optional[int] = ..., counterData: _Optional[_Union[CounterData, _Mapping]] = ..., fgBg: _Optional[int] = ...) -> None: ...

class UsageStatsExtensionProto(_message.Message):
    __slots__ = ("dataUsage",)
    DATAUSAGE_FIELD_NUMBER: _ClassVar[int]
    dataUsage: AndroidDataUsageProto
    def __init__(self, dataUsage: _Optional[_Union[AndroidDataUsageProto, _Mapping]] = ...) -> None: ...

class ModifyLibraryRequest(_message.Message):
    __slots__ = ("libraryId", "addPackageName", "removePackageName")
    LIBRARYID_FIELD_NUMBER: _ClassVar[int]
    ADDPACKAGENAME_FIELD_NUMBER: _ClassVar[int]
    REMOVEPACKAGENAME_FIELD_NUMBER: _ClassVar[int]
    libraryId: str
    addPackageName: _containers.RepeatedScalarFieldContainer[str]
    removePackageName: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, libraryId: _Optional[str] = ..., addPackageName: _Optional[_Iterable[str]] = ..., removePackageName: _Optional[_Iterable[str]] = ...) -> None: ...

class UrlRequestWrapper(_message.Message):
    __slots__ = ("developerAppsRequest",)
    DEVELOPERAPPSREQUEST_FIELD_NUMBER: _ClassVar[int]
    developerAppsRequest: DeveloperAppsRequest
    def __init__(self, developerAppsRequest: _Optional[_Union[DeveloperAppsRequest, _Mapping]] = ...) -> None: ...

class DeveloperAppsRequest(_message.Message):
    __slots__ = ("developerIdContainer1", "developerIdContainer2", "unknownInt3")
    DEVELOPERIDCONTAINER1_FIELD_NUMBER: _ClassVar[int]
    DEVELOPERIDCONTAINER2_FIELD_NUMBER: _ClassVar[int]
    UNKNOWNINT3_FIELD_NUMBER: _ClassVar[int]
    developerIdContainer1: DeveloperIdContainer
    developerIdContainer2: DeveloperIdContainer
    unknownInt3: int
    def __init__(self, developerIdContainer1: _Optional[_Union[DeveloperIdContainer, _Mapping]] = ..., developerIdContainer2: _Optional[_Union[DeveloperIdContainer, _Mapping]] = ..., unknownInt3: _Optional[int] = ...) -> None: ...

class DeveloperIdContainer(_message.Message):
    __slots__ = ("developerId", "unknownInt2", "unknownInt3")
    DEVELOPERID_FIELD_NUMBER: _ClassVar[int]
    UNKNOWNINT2_FIELD_NUMBER: _ClassVar[int]
    UNKNOWNINT3_FIELD_NUMBER: _ClassVar[int]
    developerId: str
    unknownInt2: int
    unknownInt3: int
    def __init__(self, developerId: _Optional[str] = ..., unknownInt2: _Optional[int] = ..., unknownInt3: _Optional[int] = ...) -> None: ...
