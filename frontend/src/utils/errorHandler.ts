import axios from 'axios';

export const handleApiError = (error: any): string => {
  if (axios.isAxiosError(error)) {
    if (error.response && error.response.data) {
      const errorData = error.response.data as { message: string };
      return errorData.message || 'An unexpected error occurred';
    } else if (error.request) {
      return 'No response from server';
    } else {
      return error.message;
    }
  } else {
    return 'An unexpected error occurred';
  }
};