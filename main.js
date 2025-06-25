import { fetchData } from './api.js';

export async function sendContactForm(data) {
  try {
    const result = await fetchData('/send-message', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    });

    return result;
  } catch (error) {
    throw error;
  }
}
