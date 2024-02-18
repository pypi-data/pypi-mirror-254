# Copyright CNRS/Inria/UCA
# Contributor(s): Eric Debreuve (since 2021)
#
# eric.debreuve@cnrs.fr
#
# This software is governed by the CeCILL  license under French law and
# abiding by the rules of distribution of free software.  You can  use,
# modify and/ or redistribute the software under the terms of the CeCILL
# license as circulated by CEA, CNRS and INRIA at the following URL
# "http://www.cecill.info".
#
# As a counterpart to the access to the source code and  rights to copy,
# modify and redistribute granted by the license, users are provided only
# with a limited warranty  and the software's author,  the holder of the
# economic rights,  and the successive licensors  have only  limited
# liability.
#
# In this respect, the user's attention is drawn to the risks associated
# with loading,  using,  modifying and/or developing or reproducing the
# software by the user in light of its specific status of free software,
# that may mean  that it is complicated to manipulate,  and  that  also
# therefore means  that it is reserved for developers  and  experienced
# professionals having in-depth computer knowledge. Users are therefore
# encouraged to load and test the software's suitability as regards their
# requirements in conditions enabling the security of their systems and/or
# data to be ensured and,  more generally, to use and operate it in the
# same conditions as regards security.
#
# The fact that you are presently reading this means that you have had
# knowledge of the CeCILL license and that you accept its terms.

import textwrap as text
from math import isnan as IsNaN, isinf as IsInfinity
from math import nan as NaN
from pathlib import Path as path_t
from typing import Any

from json_any.task.storage import LoadFromJSON, StoreAsJSON
from pandas import DataFrame as data_frame_t

from cell_tracking_BC.in_out.file.event import (
    NO_DIVISIONS_OR_DEATH,
    NO_EVENT_SINCE_INVALID_OR_PRUNED,
)


def SaveFeatureBookToJSON(
    feature_book: dict[(str, str), tuple[Any, ...]],
    base_path: str | path_t,
    /,
) -> None:
    """
    /!\ The feature book is modified to make all sequences the same length.
    """
    common_length = max(map(len, feature_book.values()))
    for key, value in feature_book.items():
        if (current_length := value.__len__()) < common_length:
            feature_book[key] = value + (common_length - current_length) * (NaN,)

    feature_book = data_frame_t(data=feature_book)
    feature_book.columns.set_names(("Feature", "Track Label"), inplace=True)
    feature_book.index.set_names("Time Point", inplace=True)

    if isinstance(base_path, str):
        base_path = path_t(base_path)
    if base_path.is_dir():
        base_path /= "feature-book"

    StoreAsJSON(feature_book, base_path)


def NewFeatureBookFromJSON(path: str | path_t, /) -> data_frame_t:
    """"""
    return LoadFromJSON(path)


def _AllColumnHeaders(
    feature_book: data_frame_t,
    level: int,
    /,
    *,
    as_description: bool = False,
    width: int | None = None,
    initial_indent: str = "",
    subsequent_indent: str | None = None,
) -> tuple[int | str, ...]:
    """"""
    level = feature_book.columns.names[level]
    output = tuple(sorted(set(feature_book.columns.get_level_values(level))))

    if as_description:
        description = str(output)[1:-1]
        if (output.__len__() > 0) and isinstance(output[0], str):
            description = description.replace("'", "")
        if width is not None:
            if subsequent_indent is None:
                subsequent_indent = initial_indent
            description = text.wrap(
                description,
                width=width,
                initial_indent=initial_indent,
                subsequent_indent=subsequent_indent,
            )
            description = "\n".join(description)
        output = description

    return output


def AllFeatureNames(
    feature_book: data_frame_t,
    /,
    *,
    as_description: bool = False,
    width: int | None = None,
    initial_indent: str = "",
    subsequent_indent: str | None = None,
) -> tuple[str, ...]:
    """"""
    return _AllColumnHeaders(
        feature_book,
        0,
        as_description=as_description,
        width=width,
        initial_indent=initial_indent,
        subsequent_indent=subsequent_indent,
    )


def AllTrackLabels(
    feature_book: data_frame_t,
    /,
    *,
    as_description: bool = False,
    width: int | None = None,
    initial_indent: str = "",
    subsequent_indent: str | None = None,
) -> tuple[int, ...]:
    """"""
    return _AllColumnHeaders(
        feature_book,
        1,
        as_description=as_description,
        width=width,
        initial_indent=initial_indent,
        subsequent_indent=subsequent_indent,
    )


def ValidFeatureBook(
    feature_book: data_frame_t, /
) -> tuple[data_frame_t, tuple[int, ...]]:
    """"""
    as_dict = feature_book.to_dict()
    no_event_is_nan = IsNaN(NO_EVENT_SINCE_INVALID_OR_PRUNED)
    valid_labels = tuple(
        _key[1]
        for _key, _vle in as_dict.items()
        if (_key[0] == "death time")
        and (
            ((_vle[0] != NO_EVENT_SINCE_INVALID_OR_PRUNED) and not no_event_is_nan)
            or (no_event_is_nan and not IsNaN(_vle[0]))
        )
    )
    as_dict = {_key: _vle for _key, _vle in as_dict.items() if _key[1] in valid_labels}
    # Note: Passing index= and columns= does not work like setting them below.
    valid_book = data_frame_t(data=as_dict)
    valid_book.index.set_names(feature_book.index.names, inplace="True")
    valid_book.columns.set_names(feature_book.columns.names, inplace="True")

    invalid_labels = set(AllTrackLabels(feature_book)).difference(valid_labels)

    return valid_book, tuple(sorted(invalid_labels))


def EventRelatedTrackLabels(
    feature_book: data_frame_t, event: str, /
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    """
    To be called with a valid feature book.
    """
    with_event, without_event = [], []

    event_times = feature_book[event]
    for label in AllTrackLabels(feature_book):
        first_time = event_times[label][0]
        if (first_time == NO_DIVISIONS_OR_DEATH) or (
            IsInfinity(first_time) and IsInfinity(NO_DIVISIONS_OR_DEATH)) or (
            IsNaN(first_time) and IsNaN(NO_DIVISIONS_OR_DEATH)
        ):
            which = without_event
        else:
            which = with_event
        which.append(label)

    return tuple(with_event), tuple(without_event)


def PrintFeatureBookDetails(feature_book: data_frame_t, /) -> None:
    """"""
    columns = feature_book.columns
    col_description = (
        f"{_nme}: {_lgt}" for _nme, _lgt in zip(columns.names, columns.levshape)
    )
    col_description = ", ".join(col_description)

    index = feature_book.index
    idx_description = f"[{min(index)}..{max(index)}]"

    indent = 12 * " "
    feature_names = AllFeatureNames(
        feature_book, as_description=True, width=120, initial_indent=indent
    )
    track_labels = AllTrackLabels(
        feature_book, as_description=True, width=120, initial_indent=indent
    )

    print(
        f"--- DataFrame:\n"
        f"    Columns={col_description}\n"
        f"        {columns.names[0]}:\n{feature_names}\n"
        f"        {columns.names[1]}:\n{track_labels}\n"
        f"    Index (Time Point)={idx_description}"
    )
