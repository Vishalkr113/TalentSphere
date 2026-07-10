import Select from "react-select";

export type SelectOption = {
  value: string;
  label: string;
};

type SearchSelectProps = {
  label: string;
  placeholder?: string;
  value: SelectOption | null;
  options: SelectOption[];
  isDisabled?: boolean;
  isClearable?: boolean;
  isSearchable?: boolean;
  onChange: (
    option: SelectOption | null
  ) => void;
};

function SearchSelect({
  label,
  placeholder = "Search...",
  value,
  options,
  isDisabled = false,
  isClearable = true,
  isSearchable = true,
  onChange,
}: SearchSelectProps) {
  return (
    <div className="space-y-2">

      <label className="block text-sm font-medium text-slate-700">

        {label}

      </label>

      <Select<SelectOption, false>
        value={value}
        options={options}
        placeholder={placeholder}
        isDisabled={isDisabled}
        isClearable={isClearable}
        isSearchable={isSearchable}
        onChange={(selected) =>
          onChange(selected)
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

          singleValue: (base) => ({
            ...base,
            color: "#0f172a",
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

export default SearchSelect;