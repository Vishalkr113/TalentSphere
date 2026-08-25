const configuredApiUrl = import.meta.env.VITE_API_URL?.trim();

if (!configuredApiUrl) {
  throw new Error(
    "VITE_API_URL is not configured. Copy frontend/.env.example to frontend/.env and set VITE_API_URL."
  );
}

export const API_BASE_URL = configuredApiUrl.replace(/\/$/, "");

type RequestOptions = RequestInit & {
  token?: string;
};

async function request<T>(
  endpoint: string,
  options: RequestOptions = {}
): Promise<T> {
  const { token, headers, ...rest } = options;
  const accessToken = token ?? localStorage.getItem("access_token");

  const response = await fetch(
    `${API_BASE_URL}${endpoint}`,
    {
      ...rest,
      headers: {
        ...(accessToken
          ? { Authorization: `Bearer ${accessToken}` }
          : {}),
        ...headers,
      },
    }
  );

  let data: unknown = null;

  try {
    data = await response.json();
  } catch {
    data = null;
  }

  if (!response.ok) {
    const detail = (data as { detail?: unknown } | null)?.detail;
    const message =
      typeof detail === "string"
        ? detail
        : Array.isArray(detail)
          ? detail
              .map((item) =>
                typeof item === "object" && item && "msg" in item
                  ? String((item as { msg: unknown }).msg)
                  : String(item)
              )
              .join(", ")
          : "Request failed.";

    throw new Error(message);
  }

  return data as T;
}

function jsonHeaders(): HeadersInit {
  return { "Content-Type": "application/json" };
}

export const api = {
  get<T>(endpoint: string, token?: string) {
    return request<T>(endpoint, {
      method: "GET",
      token,
    });
  },

  post<T>(endpoint: string, body?: unknown, token?: string) {
    return request<T>(endpoint, {
      method: "POST",
      token,
      headers: jsonHeaders(),
      body: body === undefined ? undefined : JSON.stringify(body),
    });
  },

  put<T>(endpoint: string, body?: unknown, token?: string) {
    return request<T>(endpoint, {
      method: "PUT",
      token,
      headers: jsonHeaders(),
      body: body === undefined ? undefined : JSON.stringify(body),
    });
  },

  patch<T>(endpoint: string, body?: unknown, token?: string) {
    return request<T>(endpoint, {
      method: "PATCH",
      token,
      headers: jsonHeaders(),
      body: body === undefined ? undefined : JSON.stringify(body),
    });
  },

  delete<T>(endpoint: string, token?: string) {
    return request<T>(endpoint, {
      method: "DELETE",
      token,
    });
  },
};

export { request };
