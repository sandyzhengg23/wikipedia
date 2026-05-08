import http from 'k6/http';
import { sleep, check } from 'k6';

export const options = {
  stages: [
    { duration: '20s', target: 10 },
    { duration: '10s', target: 50 },
    { duration: '30s', target: 50 },
    { duration: '10s', target: 10 },
    { duration: '20s', target: 0 },
  ],

  thresholds: {
    http_req_duration: ['p(95)<1000'],
    http_req_failed: ['rate<0.01'],
    http_reqs: ['rate>5'],
  },
};

export default function () {
  const res = http.get('https://www.wikipedia.org/');

  check(res, {
    'status is 200': (r) => r.status === 200,
    'page contains Wikipedia': (r) => r.body.includes('Wikipedia'),
  });

  sleep(1);
}