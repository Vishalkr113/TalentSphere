import { useEffect, useState } from "react";
import { Country, State, City } from "country-state-city";

import SearchSelect, {
  type SelectOption,
} from "../Select/SearchSelect";

export interface Address {
  country: string;
  state: string;
  district: string;
  city: string;
  pinCode: string;
}

interface AddressSelectorProps {
  value: Address;
  disabled?: boolean;
  onChange: (value: Address) => void;
}

function AddressSelector({
  value,
  disabled = false,
  onChange,
}: AddressSelectorProps) {
  const [countries, setCountries] = useState<SelectOption[]>([]);
  const [states, setStates] = useState<SelectOption[]>([]);
  const [cities, setCities] = useState<SelectOption[]>([]);

  useEffect(() => {
    setCountries(
      Country.getAllCountries().map((country) => ({
        value: country.isoCode,
        label: country.name,
      }))
    );
  }, []);

  useEffect(() => {
    if (!value.country) {
      setStates([]);
      return;
    }

    setStates(
      State.getStatesOfCountry(value.country).map((state) => ({
        value: state.isoCode,
        label: state.name,
      }))
    );
  }, [value.country]);

  useEffect(() => {
    if (!value.country || !value.state) {
      setCities([]);
      return;
    }

    setCities(
      City.getCitiesOfState(value.country, value.state).map((city) => ({
        value: city.name,
        label: city.name,
      }))
    );
  }, [value.country, value.state]);

  return (
    <div className="grid gap-6 md:grid-cols-3">

      <SearchSelect
        label="Country"
        options={countries}
        value={
          countries.find(
            (c) => c.value === value.country
          ) || null
        }
        isDisabled={disabled}
        onChange={(option) =>
          onChange({
            country: option?.value || "",
            state: "",
            district: "",
            city: "",
            pinCode: "",
          })
        }
      />

      <SearchSelect
        label="State"
        options={states}
        value={
          states.find(
            (s) => s.value === value.state
          ) || null
        }
        isDisabled={disabled || !value.country}
        onChange={(option) =>
          onChange({
            ...value,
            state: option?.value || "",
            district: "",
            city: "",
          })
        }
      />

      <SearchSelect
        label="City"
        options={cities}
        value={
          cities.find(
            (c) => c.value === value.city
          ) || null
        }
        isDisabled={
          disabled ||
          !value.country ||
          !value.state
        }
        onChange={(option) =>
          onChange({
            ...value,
            district: option?.label || "",
            city: option?.value || "",
          })
        }
      />

    </div>
  );
}

export default AddressSelector;