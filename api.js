// src/utils/api.js

export async function fetchData(url, options = {}) {
  try {
    const response = await fetch(url, options);

    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }

    // Handle no content (204)
    if (response.status === 204) {
      return null;
    }

    const contentType = response.headers.get("content-type");

    if (contentType && contentType.includes("application/json")) {
      return await response.json();
    }

    console.warn(`Response from ${url} was not JSON. Returning as text.`);
    return await response.text();

  } catch (error) {
    console.error(`Error fetching ${url}:`, error);
    throw error;
  }
}
