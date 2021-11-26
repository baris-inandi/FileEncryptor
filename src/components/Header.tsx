import { Button, Heading, Stack, Text } from "@chakra-ui/core"

const Header: React.FC = () => {
    return (
        <Stack spacing={4} bg="white" p={8} borderRadius="lg">
            <Heading as="h1" size="2xl" color="blue.500">
            Chakra UI is rad!
            </Heading>
            <Text as="p" fontSize="md" color="blue.400">
            Here are your first Chakra components:
            </Text>
            <Button isFullWidth>
            Click me, please!
            </Button>
        </Stack>  
    )
}

export default Header
