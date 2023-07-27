import aiohttp
import asyncio
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Replace this with the base URL of your server
BASE_URL = "http://localhost:80"

# Function to send a single request and log the response time
async def send_request(session, request_number):
    url = f"{BASE_URL}/"  # Replace "your_endpoint_here" with your specific API endpoint
    try:
        start_time = time.time()
        async with session.get(url) as response:
            response_time = time.time() - start_time
            logging.info(f"Request {request_number} - Response time: {response_time:.2f} seconds")
            return response_time
    except aiohttp.ClientError as e:
        logging.error(f"Request {request_number} - Error: {e}")
        return None

# Function to send multiple requests in parallel
async def send_requests_in_parallel(total_requests, parallel_requests):
    async with aiohttp.ClientSession() as session:
        tasks = [send_request(session, i) for i in range(1, total_requests + 1)]
        response_times = await asyncio.gather(*tasks)
        return response_times

def main():
    total_requests = 1000
    parallel_requests = 10

    logging.info("Sending requests...")

    loop = asyncio.get_event_loop()
    response_times = loop.run_until_complete(send_requests_in_parallel(total_requests, parallel_requests))

    # Calculate some statistics about the response times
    valid_response_times = [time for time in response_times if time is not None]
    average_response_time = sum(valid_response_times) / len(valid_response_times)
    max_response_time = max(valid_response_times)
    min_response_time = min(valid_response_times)

    logging.info(f"Total Requests: {total_requests}")
    logging.info(f"Parallel Requests: {parallel_requests}")
    logging.info(f"Average Response Time: {average_response_time:.2f} seconds")
    logging.info(f"Maximum Response Time: {max_response_time:.2f} seconds")
    logging.info(f"Minimum Response Time: {min_response_time:.2f} seconds")

if __name__ == "__main__":
    main()
