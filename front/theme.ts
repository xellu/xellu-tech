
import type { CustomThemeConfig } from '@skeletonlabs/tw-plugin';

export const appTheme: CustomThemeConfig = {
    name: 'app-theme',
    properties: {
		// =~= Theme Properties =~=
		"--theme-font-family-base": `"VT323", monospace`,
		"--theme-font-family-heading": `"VT323", monospace`,
		"--theme-font-color-base": "255 255 255",
		"--theme-font-color-dark": "255 255 255",
		"--theme-rounded-base": "0px",
		"--theme-rounded-container": "0px",
		"--theme-border-base": "1px",
		// =~= Theme On-X Colors =~=
		"--on-primary": "0 0 0",
		"--on-secondary": "0 0 0",
		"--on-tertiary": "0 0 0",
		"--on-success": "0 0 0",
		"--on-warning": "0 0 0",
		"--on-error": "0 0 0",
		"--on-surface": "255 255 255",
		// =~= Theme Colors  =~=
		// primary | #00ff00 
		"--color-primary-50": "217 255 217", // #d9ffd9
		"--color-primary-100": "204 255 204", // #ccffcc
		"--color-primary-200": "191 255 191", // #bfffbf
		"--color-primary-300": "153 255 153", // #99ff99
		"--color-primary-400": "77 255 77", // #4dff4d
		"--color-primary-500": "0 255 0", // #00ff00
		"--color-primary-600": "0 230 0", // #00e600
		"--color-primary-700": "0 191 0", // #00bf00
		"--color-primary-800": "0 153 0", // #009900
		"--color-primary-900": "0 125 0", // #007d00
		// secondary | #00ffff 
		"--color-secondary-50": "217 255 255", // #d9ffff
		"--color-secondary-100": "204 255 255", // #ccffff
		"--color-secondary-200": "191 255 255", // #bfffff
		"--color-secondary-300": "153 255 255", // #99ffff
		"--color-secondary-400": "77 255 255", // #4dffff
		"--color-secondary-500": "0 255 255", // #00ffff
		"--color-secondary-600": "0 230 230", // #00e6e6
		"--color-secondary-700": "0 191 191", // #00bfbf
		"--color-secondary-800": "0 153 153", // #009999
		"--color-secondary-900": "0 125 125", // #007d7d
		// tertiary | #ff00ff 
		"--color-tertiary-50": "255 217 255", // #ffd9ff
		"--color-tertiary-100": "255 204 255", // #ffccff
		"--color-tertiary-200": "255 191 255", // #ffbfff
		"--color-tertiary-300": "255 153 255", // #ff99ff
		"--color-tertiary-400": "255 77 255", // #ff4dff
		"--color-tertiary-500": "255 0 255", // #ff00ff
		"--color-tertiary-600": "230 0 230", // #e600e6
		"--color-tertiary-700": "191 0 191", // #bf00bf
		"--color-tertiary-800": "153 0 153", // #990099
		"--color-tertiary-900": "125 0 125", // #7d007d
		// success | #00ff00 
		"--color-success-50": "217 255 217", // #d9ffd9
		"--color-success-100": "204 255 204", // #ccffcc
		"--color-success-200": "191 255 191", // #bfffbf
		"--color-success-300": "153 255 153", // #99ff99
		"--color-success-400": "77 255 77", // #4dff4d
		"--color-success-500": "0 255 0", // #00ff00
		"--color-success-600": "0 230 0", // #00e600
		"--color-success-700": "0 191 0", // #00bf00
		"--color-success-800": "0 153 0", // #009900
		"--color-success-900": "0 125 0", // #007d00
		// warning | #ffff00 
		"--color-warning-50": "255 255 217", // #ffffd9
		"--color-warning-100": "255 255 204", // #ffffcc
		"--color-warning-200": "255 255 191", // #ffffbf
		"--color-warning-300": "255 255 153", // #ffff99
		"--color-warning-400": "255 255 77", // #ffff4d
		"--color-warning-500": "255 255 0", // #ffff00
		"--color-warning-600": "230 230 0", // #e6e600
		"--color-warning-700": "191 191 0", // #bfbf00
		"--color-warning-800": "153 153 0", // #999900
		"--color-warning-900": "125 125 0", // #7d7d00
		// error | #ff0000 
		"--color-error-50": "255 217 217", // #ffd9d9
		"--color-error-100": "255 204 204", // #ffcccc
		"--color-error-200": "255 191 191", // #ffbfbf
		"--color-error-300": "255 153 153", // #ff9999
		"--color-error-400": "255 77 77", // #ff4d4d
		"--color-error-500": "255 0 0", // #ff0000
		"--color-error-600": "230 0 0", // #e60000
		"--color-error-700": "191 0 0", // #bf0000
		"--color-error-800": "153 0 0", // #990000
		"--color-error-900": "125 0 0", // #7d0000
		// surface | #000a00 
		"--color-surface-50": "217 218 217", // #d9dad9
		"--color-surface-100": "204 206 204", // #cccecc
		"--color-surface-200": "191 194 191", // #bfc2bf
		"--color-surface-300": "153 157 153", // #999d99
		"--color-surface-400": "77 84 77", // #4d544d
		"--color-surface-500": "0 10 0", // #000a00
		"--color-surface-600": "0 9 0", // #000900
		"--color-surface-700": "0 8 0", // #000800
		"--color-surface-800": "0 6 0", // #000600
		"--color-surface-900": "0 5 0", // #000500
		
	}
}