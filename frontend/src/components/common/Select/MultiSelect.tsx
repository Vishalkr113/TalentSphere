import Select from "react-select";

import type { SelectOption } from "./SearchSelect";

type MultiSelectProps = {
  label: string;
  placeholder?: string;
  value: SelectOption[];
  options: SelectOption[];
  isDisabled?: boolean;
  onChange: (
    options: SelectOption[]
  ) => void;
};

function MultiSelect({
  label,
  placeholder = "Search...",
  value,
  options,
  isDisabled = false,
  onChange,
}: MultiSelectProps) {
  return (
    <div className="space-y-2">

      <label className="block text-sm font-medium text-slate-700">

        {label}

      </label>

      <Select<SelectOption, true>
        isMulti
        value={value}
        options={options}
        placeholder={placeholder}
        isDisabled={isDisabled}
        closeMenuOnSelect={false}
        hideSelectedOptions={false}
        onChange={(selected) =>
          onChange(
            selected
              ? [...selected]
              : []
          )
        }
        styles={{
          control: (base, state) => ({
            ...base,
            minHeight: 52,
            borderRadius: 14,
            borderColor: state.isFocused
              ? "#06b6d4"
              : "#cbd5e1",
            boxShadow: state.isFocused
              ? "0 0 0 4px rgba(6,182,212,.15)"
              : "none",
            "&:hover": {
              borderColor: "#06b6d4",
            },
          }),

          menu: (base) => ({
            ...base,
            borderRadius: 14,
            overflow: "hidden",
            zIndex: 9999,
          }),

          option: (base, state) => ({
            ...base,
            backgroundColor: state.isFocused
              ? "#ecfeff"
              : "#ffffff",
            color: "#0f172a",
            cursor: "pointer",
            paddingTop: 12,
            paddingBottom: 12,
          }),

          placeholder: (base) => ({
            ...base,
            color: "#94a3b8",
          }),

          multiValue: (base) => ({
            ...base,
            backgroundColor:
              "#cffafe",
            borderRadius: 8,
          }),

          multiValueLabel: (base) => ({
            ...base,
            color: "#155e75",
            fontWeight: 600,
          }),

          multiValueRemove: (base) => ({
            ...base,
            color: "#155e75",
            ":hover": {
              backgroundColor:
                "#06b6d4",
              color: "#ffffff",
            },
          }),

          indicatorSeparator: () => ({
            display: "none",
          }),

          dropdownIndicator: (base) => ({
            ...base,
            color: "#06b6d4",
          }),
        }}
      />

    </div>
  );
}

export default MultiSelect;