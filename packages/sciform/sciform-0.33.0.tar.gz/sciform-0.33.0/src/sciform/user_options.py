"""UserOptions Dataclass which stores user input."""


from __future__ import annotations

from dataclasses import InitVar, asdict, dataclass
from typing import get_args

from sciform import global_options, modes
from sciform.rendered_options import RenderedOptions


@dataclass(frozen=True)
class UserOptions:
    """Dataclass storing user input."""

    exp_mode: modes.ExpMode | None = None
    exp_val: int | type(modes.AutoExpVal) | None = None
    round_mode: modes.RoundMode | None = None
    ndigits: int | type(modes.AutoDigits) | None = None
    upper_separator: modes.UpperSeparators | None = None
    decimal_separator: modes.DecimalSeparators | None = None
    lower_separator: modes.LowerSeparators | None = None
    sign_mode: modes.SignMode | None = None
    left_pad_char: modes.LeftPadChar | None = None
    left_pad_dec_place: int | None = None
    exp_format: modes.ExpFormat | None = None
    extra_si_prefixes: dict[int, str] | None = None
    extra_iec_prefixes: dict[int, str] | None = None
    extra_parts_per_forms: dict[int, str] | None = None
    capitalize: bool | None = None
    superscript: bool | None = None
    nan_inf_exp: bool | None = None
    paren_uncertainty: bool | None = None
    pdg_sig_figs: bool | None = None
    left_pad_matching: bool | None = None
    paren_uncertainty_separators: bool | None = None
    pm_whitespace: bool | None = None

    add_c_prefix: InitVar[bool] = False
    add_small_si_prefixes: InitVar[bool] = False
    add_ppth_form: InitVar[bool] = False

    def __post_init__(
        self: UserOptions,
        add_c_prefix: bool,  # noqa: FBT001
        add_small_si_prefixes: bool,  # noqa: FBT001
        add_ppth_form: bool,  # noqa: FBT001
    ) -> None:
        self.populate_dicts(
            add_c_prefix=add_c_prefix,
            add_small_si_prefixes=add_small_si_prefixes,
            add_ppth_form=add_ppth_form,
        )
        self.validate(self)

    def populate_dicts(  # noqa: C901
        self: UserOptions,
        *,
        add_c_prefix: bool,
        add_small_si_prefixes: bool,
        add_ppth_form: bool,
    ) -> None:
        """Populate extra prefix translations from user input flags."""
        if add_c_prefix:
            if self.extra_si_prefixes is None:
                super().__setattr__("extra_si_prefixes", {})
            if -2 not in self.extra_si_prefixes:
                self.extra_si_prefixes[-2] = "c"

        if add_small_si_prefixes:
            if self.extra_si_prefixes is None:
                super().__setattr__("extra_si_prefixes", {})
            if -2 not in self.extra_si_prefixes:
                self.extra_si_prefixes[-2] = "c"
            if -1 not in self.extra_si_prefixes:
                self.extra_si_prefixes[-1] = "d"
            if +1 not in self.extra_si_prefixes:
                self.extra_si_prefixes[+1] = "da"
            if +2 not in self.extra_si_prefixes:
                self.extra_si_prefixes[+2] = "h"

        if add_ppth_form:
            if self.extra_parts_per_forms is None:
                super().__setattr__("extra_parts_per_forms", {})
            if -3 not in self.extra_parts_per_forms:
                self.extra_parts_per_forms[-3] = "ppth"

    @staticmethod
    def validate(options: UserOptions | RenderedOptions) -> None:
        """Validate user inputs."""
        if (
            options.round_mode == "sig_fig"
            and isinstance(options.ndigits, int)
            and options.ndigits < 1
        ):
            msg = f"ndigits must be >= 1 for sig fig rounding, not {options.ndigits}."
            raise ValueError(msg)

        if options.exp_val is not modes.AutoExpVal and options.exp_val is not None:
            if options.exp_mode in ["fixed_point", "percent"] and options.exp_val != 0:
                msg = (
                    f"Exponent must must be 0, not exp_val={options.exp_val}, for "
                    f"fixed point and percent exponent modes."
                )
                raise ValueError(msg)
            if (
                options.exp_mode in ["engineering", "engineering_shifted"]
                and options.exp_val % 3 != 0
            ):
                msg = (
                    f"Exponent must be a multiple of 3, not exp_val={options.exp_val}, "
                    f"for engineering exponent modes."
                )
                raise ValueError(msg)
            if options.exp_mode == "binary_iec" and options.exp_val % 10 != 0:
                msg = (
                    f"Exponent must be a multiple of 10, not "
                    f"exp_val={options.exp_val}, for binary IEC exponent mode."
                )
                raise ValueError(msg)

        UserOptions.validate_separators(options)

    @staticmethod
    def validate_separators(options: UserOptions | RenderedOptions) -> None:
        """Validate separator user input."""
        if options.upper_separator is not None:
            if options.upper_separator not in get_args(modes.UpperSeparators):
                msg = (
                    f"upper_separator must be in "
                    f"{get_args(modes.UpperSeparators)}, not "
                    f"{options.upper_separator}."
                )
                raise ValueError(msg)
            if options.upper_separator == options.decimal_separator:
                msg = (
                    f"upper_separator and decimal_separator "
                    f"({options.upper_separator}) cannot be equal."
                )
                raise ValueError(msg)

        if options.decimal_separator is not None and (
            options.decimal_separator not in get_args(modes.DecimalSeparators)
        ):
            msg = (
                f"decimal_separator must be in "
                f"{get_args(modes.DecimalSeparators)}, not "
                f"{options.decimal_separator}."
            )
            raise ValueError(msg)

        if options.lower_separator is not None and (
            options.lower_separator not in get_args(modes.LowerSeparators)
        ):
            msg = (
                f"lower_separator must be in {get_args(modes.LowerSeparators)}, "
                f"not {options.lower_separator}."
            )
            raise ValueError(msg)

    def render(self: UserOptions) -> RenderedOptions:
        """Render UserOptions into RenderedOptions."""
        key_to_enum_dict = {
            "exp_mode": modes.ExpModeEnum,
            "round_mode": modes.RoundModeEnum,
            "upper_separator": modes.SeparatorEnum,
            "decimal_separator": modes.SeparatorEnum,
            "lower_separator": modes.SeparatorEnum,
            "sign_mode": modes.SignModeEnum,
            "left_pad_char": modes.LeftPadCharEnum,
            "exp_format": modes.ExpFormatEnum,
        }

        global_defaults_dict = asdict(global_options.GLOBAL_DEFAULT_OPTIONS)
        kwargs = {}
        for key, value in asdict(self).items():
            if value is None:
                rendered_value = global_defaults_dict[key]
            elif isinstance(value, str):
                enum = key_to_enum_dict[key]
                rendered_value = modes.mode_str_to_enum(value, enum)
            else:
                rendered_value = value
            kwargs[key] = rendered_value
        rendered_options = RenderedOptions(**kwargs)
        self.validate(rendered_options)
        return rendered_options
