import { FC } from "react"
import { ThemeProvider } from "@chakra-ui/core"
import { theme } from "@chakra-ui/core"

const FEXThemeProvider : FC = (props) => {
    return <ThemeProvider theme={theme}>{props.children}</ThemeProvider>
}

export default FEXThemeProvider