export function info(message: string) {
    console.info(`%c[XelOS] %c${message}`, `color: #00ffff`, `color: #fff`)
}

export function warn(message: string) {
    console.warn(`%c[XelOS] %c${message}`, `color: #ffff00`, `color: #fff`)
}

export function error(message: string) {
    console.error(`%c[XelOS] %c${message}`, `color: #ff0000`, `color: #fff`)
}

export function success(message: string) {
    console.log(`%c[XelOS] %c${message}`, `color: #00ff00`, `color: #fff`)
}

export function log(message: string) {
    console.log(`%c[XelOS] %c${message}`, `color: #ffffff`, `color: #fff`)
}

export let logger = {
    info,
    success,
    warn,
    error,
    log
}